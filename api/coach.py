"""Free local Ollama bridge; never forwards student data to a paid third-party API."""
import json,os,re,urllib.request,urllib.error,base64,tempfile
from http.server import BaseHTTPRequestHandler
OLLAMA=os.environ.get('OLLAMA_URL','http://127.0.0.1:11434')
MODEL=os.environ.get('OLLAMA_MODEL','llama3.2:3b')
def complete(system,prompt):
    req=urllib.request.Request(OLLAMA+'/api/chat',data=json.dumps({'model':MODEL,'stream':False,'messages':[{'role':'system','content':system},{'role':'user','content':prompt}],'options':{'temperature':0.4,'num_predict':550}}).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=65) as r: return json.load(r)['message']['content']
def respond(data):
    kind=data.get('kind')
    if kind=='mentor':
        system='You are a supportive, concise career mentor for Indian college students. Give specific next steps, adapt to the selected career track, do not promise placements. Ask one helpful follow-up question. Do not pretend to know private student data.'
        return {'source':'ollama','reply':complete(system,json.dumps({k:data.get(k) for k in ('track','goal','level','skill','hours','message','plan')},ensure_ascii=False)[:12000])}
    if kind=='interview':
        system='You are a realistic technical interviewer. Evaluate the student answer against the question, highlight concrete strengths and gaps. Ask exactly one contextual follow-up based on their actual answer. Never claim this is an official interview. Output valid JSON with keys feedback and followup, both strings.'
        raw=complete(system,json.dumps({k:data.get(k) for k in ('track','company','difficulty','language','mode','question','answer','focus','history')},ensure_ascii=False)[:12000]);raw=re.sub(r'^```(?:json)?\s*|\s*```$','',raw.strip());
        try:
            out=json.loads(raw);return {'source':'ollama','feedback':str(out['feedback']),'followup':str(out['followup'])}
        except Exception:return {'source':'ollama','feedback':raw[:1800],'followup':'Can you discuss a trade-off or edge case in your answer?'}
    if kind=='review':
        system='You review student assignment evidence. Give actionable feedback with clear limitations. Do not claim code was executed or tests were verified. Output concise plain text: strengths, gaps, next steps.'
        return {'source':'ollama','feedback':complete(system,json.dumps({k:data.get(k) for k in ('track','brief','submission')},ensure_ascii=False)[:14000])}
    raise ValueError('Invalid kind')
class handler(BaseHTTPRequestHandler):
    def _send(self,status,obj):
        b=json.dumps(obj).encode();self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Access-Control-Allow-Origin','*');self.send_header('Content-Length',str(len(b)));self.end_headers();self.wfile.write(b)
    def do_GET(self):
        if self.path=='/api/health':
            try:
                with urllib.request.urlopen(OLLAMA+'/api/tags',timeout=2) as r: names=[m['name'] for m in json.load(r).get('models',[])];available=any(x==MODEL or x.startswith(MODEL+':') for x in names)
            except Exception:available=False
            self._send(200,{'ollama':available,'model':MODEL})
        else:self._send(404,{'error':'Not found'})
    def do_POST(self):
        if self.path=='/api/transcribe':
            try:
                n=int(self.headers.get('Content-Length','0'))
                if n<1 or n>13000000:return self._send(413,{'error':'Recording too large (maximum 9 MB).'})
                payload=json.loads(self.rfile.read(n));audio=base64.b64decode(payload.get('audio',''),validate=True)
                if len(audio)<1000 or len(audio)>9*1024*1024:raise ValueError('Audio is empty or too large')
                try:from faster_whisper import WhisperModel
                except ImportError:return self._send(503,{'error':'Install free local transcription: pip install faster-whisper'})
                if not hasattr(handler,'whisper_model'):handler.whisper_model=WhisperModel(os.environ.get('WHISPER_MODEL','tiny.en'),device='cpu',compute_type='int8')
                suffix='.mp4' if 'mp4' in payload.get('mime','') else '.webm'
                with tempfile.NamedTemporaryFile(suffix=suffix,delete=False) as tmp:tmp.write(audio);path=tmp.name
                try:
                    segments,info=handler.whisper_model.transcribe(path,beam_size=3,vad_filter=True,language='en');transcript=' '.join(x.text.strip() for x in segments).strip()
                finally:os.unlink(path)
                return self._send(200,{'text':transcript,'source':'local faster-whisper'})
            except Exception as e:return self._send(400,{'error':str(e)[:250]})
        if self.path!='/api/coach':return self._send(404,{'error':'Not found'})
        try:
            n=int(self.headers.get('Content-Length','0'))
            if n<1 or n>35000:return self._send(413,{'error':'Request too large'})
            data=json.loads(self.rfile.read(n));self._send(200,respond(data))
        except (urllib.error.URLError,TimeoutError) as e:self._send(503,{'error':'Local Ollama unavailable','detail':str(e)[:160]})
        except Exception as e:self._send(400,{'error':str(e)[:180]})
