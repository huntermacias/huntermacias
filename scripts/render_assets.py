from pathlib import Path
from xml.sax.saxutils import escape
P=Path(__file__).resolve().parents[1]; A=P/'assets'
colors={
 'dark':dict(bg='#0A0F17',panel='#101925',panel2='#162130',border='#2A394B',ink='#F1F5FB',muted='#96A6BB',faint='#617187',accent='#8891FF',a2='#66CDBA',warm='#F0B96D',red='#EE7989',grid='#243246',ghost='#1D2B3C'),
 'light':dict(bg='#F7F9FC',panel='#FFFFFF',panel2='#EDF3F9',border='#D7DFE9',ink='#18243A',muted='#5B6C81',faint='#8191A6',accent='#596ADA',a2='#158E7F',warm='#B47B31',red='#C75E6F',grid='#D5DFEA',ghost='#E8EEF5')}

# Framework avoids dependency on external assets and fonts.
def svg_open(w,h,title,desc,c):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t d">
<title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc>
<style>
 text{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;}}
 .mono{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;}}
 .pulse{{animation:pulse 3.4s ease-in-out infinite; transform-origin:center;}}
 .blink{{animation:blink 2.4s ease-in-out infinite;}}
 .trace{{stroke-dasharray:9 14;animation:dash 13s linear infinite;}}
 .sweep{{animation:sweep 8s ease-in-out infinite;}}
 .rise{{animation:rise 4.6s ease-in-out infinite;}}
 @keyframes pulse{{0%,100%{{opacity:0.42}}50%{{opacity:1}}}}
 @keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:.35}}}}
 @keyframes dash{{to{{stroke-dashoffset:-230}}}}
 @keyframes sweep{{0%{{opacity:0}}15%{{opacity:.60}}55%{{opacity:.20}}100%{{opacity:0}}}}
 @keyframes rise{{0%,100%{{opacity:0.45}}45%{{opacity:0.95}}}}
 @media (prefers-reduced-motion:reduce){{.pulse,.blink,.trace,.sweep,.rise{{animation:none}}}}
</style>'''

def label(x,y,t,color,size=13,cls='',weight=500):return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" class="{cls}">{escape(t)}</text>'
def line(x1,y1,x2,y2,color,op=.8,dash=None,w=1):return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" opacity="{op}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def rect(x,y,w,h,fill,stroke='none',r=0,stroke_w=1):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_w}"/>'
def circle(x,y,r,fill,stroke='none',sw=1,cls=''):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" class="{cls}"/>'

def make_hero(theme):
 c=colors[theme]; s=svg_open(1200,395,'Hunter Macias — software engineer and product builder','Editorial profile masthead with animated execution traces and system signals.',c)
 s+=f'''<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c['bg']}"/><stop offset="1" stop-color="{c['panel']}"/></linearGradient><linearGradient id="glow" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c['accent']}" stop-opacity=".22"/><stop offset="1" stop-color="{c['a2']}" stop-opacity=".04"/></linearGradient><linearGradient id="track" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c['accent']}"/><stop offset="1" stop-color="{c['a2']}"/></linearGradient><clipPath id="clip"><rect x="0" y="0" width="1200" height="395" rx="20"/></clipPath></defs>'''
 s+=rect(1,1,1198,393,'url(#bg)',c['border'],20,2)
 s+='<g clip-path="url(#clip)">'
 # Detail grid only on right, avoids busy left.
 for x in range(656,1210,31):s+=line(x,26,x,390,c['grid'],.28)
 for y in range(26,410,31):s+=line(650,y,1210,y,c['grid'],.28)
 s+=rect(650,0,550,395,'url(#glow)')
 s+=rect(55,46,9,9,c['a2'],r=3)+label(75,55,'ENGINEER  /  BUILDER  /  TEACHER',c['muted'],13,'mono',600)
 s+=label(56,163,'HUNTER',c['ink'],84,weight=760)
 s+=label(56,246,'MACIAS',c['ink'],84,weight=760)
 s+=line(56,272,530,272,c['border'],1,w=2)
 s+=label(57,304,'Making complex systems',c['muted'],23,weight=500)
 s+=label(57,333,'easier to understand and improve.',c['muted'],23,weight=500)
 s+=label(57,369,'SEATTLE, WA   ·   BUILDING SPIKEPROOF',c['faint'],13,'mono',500)
 # Right system illustration.
 s+=rect(703,58,439,269,c['panel'],c['border'],15,1.5)
 s+=circle(725,79,3.5,c['red'])+circle(739,79,3.5,c['warm'])+circle(753,79,3.5,c['a2'])
 s+=label(800,84,'SIGNALS / THE SYSTEM',c['muted'],13,'mono',600)
 s+=label(721,128,'request path',c['faint'],13,'mono')
 s+=label(1070,128,'trace #01',c['faint'],12,'mono')
 # central circular nodes and connection 
 pts=[(744,192),(848,166),(957,202),(1090,160)]
 d='M744 192 L848 166 L957 202 L1090 160'
 s+=f'<path d="{d}" stroke="{c["border"]}" stroke-width="10" stroke-linecap="round" fill="none" opacity=".32"/>'
 s+=f'<path d="{d}" stroke="{c["accent"]}" stroke-width="2.5" fill="none" class="trace" opacity=".85"/>'
 for i,(x,y) in enumerate(pts):
  col=c['accent'] if i!=3 else c['a2'];s+=circle(x,y,18,c['panel2'],c['border'],1.4)
  s+=circle(x,y,5,col)+circle(x,y,10,'none',col,1.5,'pulse')
 for x,y,t in [(719,228,'INPUT'),(814,209,'EXECUTE'),(917,245,'MEASURE'),(1057,204,'UNDERSTAND')]:s+=label(x,y,t,c['muted'],10,'mono')
 # Bottom telemetry
 s+=line(721,268,1120,268,c['border'],.8)
 s+=label(723,292,'PERFORMANCE',c['faint'],10,'mono')
 s+=label(910,292,'RELIABILITY',c['faint'],10,'mono')
 s+=label(1080,292,'UX',c['faint'],10,'mono')
 s+=rect(720,307,150,3,c['grid'],r=1)+rect(720,307,94,3,c['accent'],r=1)
 s+=rect(906,307,125,3,c['grid'],r=1)+rect(906,307,91,3,c['a2'],r=1)
 s+=rect(1064,307,55,3,c['grid'],r=1)+rect(1064,307,45,3,c['warm'],r=1)
 s+=circle(1128,82,4,c['a2'],cls='blink')
 s+='</g></svg>'
 (A/f'hero-{theme}.svg').write_text(s)

def make_spikeproof(theme):
 c=colors[theme]; s=svg_open(1200,414,'Spikeproof — performance engineering workbench','A conceptual system journey and diagnostics visualization, illustrating API, browser, load and evidence.',c)
 s+=f'''<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c['panel']}"/><stop offset="1" stop-color="{c['bg']}"/></linearGradient><linearGradient id="flow" x1="0" x2="1"><stop stop-color="{c['accent']}"/><stop offset="1" stop-color="{c['a2']}"/></linearGradient></defs>'''
 s+=rect(1,1,1198,412,'url(#bg)',c['border'],17,2)
 s+=rect(34,32,48,48,c['accent'],r=12)
 s+=f'<path d="M46 57 H53 L59 45 L66 66 L73 54 H78" fill="none" stroke="{c["bg"]}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>'
 s+=label(96,60,'SPIKEPROOF',c['ink'],28,weight=760)
 s+=label(37,119,'Performance engineering,',c['ink'],28,weight=700)
 s+=label(37,154,'without the friction.',c['ink'],28,weight=700)
 s+=label(38,190,'Design journeys. Apply load. Investigate',c['muted'],17)
 s+=label(38,214,'what your system actually did.',c['muted'],17)
 # characteristic statements.
 for i,(t,co) in enumerate([('API + browser journeys',c['accent']),('k6 load execution',c['a2']),('evidence-driven analysis',c['warm'])]):
  y=259+35*i;s+=circle(42,y-4,4,co)+label(56,y,t,c['ink'],16,weight=540)
 s+=label(37,383,'INDEPENDENT PRODUCT  /  PRIVATE SOURCE',c['faint'],12,'mono')
 # right mock app frame
 s+=rect(510,32,656,349,c['bg'],c['border'],13,1.5)
 s+=rect(511,33,654,42,c['panel2'],r=12)
 s+=line(511,75,1164,75,c['border'],1)
 s+=circle(532,54,4,c['a2'])+label(545,59,'JOURNEY  /  TRACE EXPLORER',c['muted'],12,'mono',600)
 s+=rect(1058,45,86,19,c['panel'],c['border'],5)+label(1072,59,'RUN  /  01',c['muted'],10,'mono')
 # service path
 stages=[(550,'Client',c['accent']),(700,'API',c['accent']),(850,'Worker',c['a2']),(1017,'Evidence',c['warm'])]
 s+=label(540,112,'01 / EXECUTION PATH',c['faint'],12,'mono')
 for i,(x,name,col) in enumerate(stages):
  s+=rect(x,132,114,47,c['panel2'],c['border'],9)
  s+=circle(x+17,154,5,col,cls='pulse')+label(x+29,160,name,c['ink'],13,weight=640)
  if i<len(stages)-1:
   nextx=stages[i+1][0];s+=line(x+114,155,nextx,155,c['border'],1.5,w=2)
   s+=f'<path d="M{x+114} 155 L{nextx} 155" stroke="{c["a2"]}" stroke-width="2" fill="none" class="trace"/>'
 # combined metrics chart, illustrative
 s+=label(540,217,'02 / PERFORMANCE EVIDENCE',c['faint'],12,'mono')
 s+=rect(539,233,595,123,c['panel'],c['border'],7)
 for y in [252,283,314,345]:s+=line(552,y,1124,y,c['grid'],.85)
 for x in [572,650,728,806,884,962,1040,1118]:s+=line(x,243,x,346,c['grid'],.4)
 s+=f'<path d="M554 326 L588 322 L624 315 L661 318 L700 309 L737 312 L774 293 L812 289 L849 280 L886 279 L922 265 L960 270 L998 260 L1036 258 L1073 249 L1117 241" fill="none" stroke="{c["accent"]}" stroke-width="2.9" stroke-linejoin="round"/>'
 s+=f'<path d="M554 333 L588 330 L624 332 L661 327 L700 326 L737 327 L774 323 L812 324 L849 320 L886 323 L922 317 L960 318 L998 315 L1036 319 L1073 312 L1117 307" fill="none" stroke="{c["a2"]}" stroke-width="2" stroke-linejoin="round"/>'
 s+=line(552,286,1124,286,c['warm'],.7,'4 5')
 s+=label(552,370,'illustrative visualization · no live production data',c['faint'],10,'mono')
 s+='</svg>'; (A/f'spikeproof-{theme}.svg').write_text(s)

def make_footer(theme):
 c=colors[theme];s=svg_open(1200,90,'Build, measure, learn, repeat','A restrained animated signal closing the profile.',c)
 s+=rect(1,1,1198,88,c['bg'],c['border'],12,2)
 s+=label(36,53,'BUILD  /  MEASURE  /  LEARN  /  REPEAT',c['ink'],18,'mono',600)
 s+=line(630,46,1138,46,c['border'],1,w=2)
 s+=f'<path d="M630 46 L755 46 L778 33 L798 59 L820 46 L940 46 L967 27 L993 65 L1017 46 L1138 46" stroke="{c["a2"]}" stroke-width="2.7" stroke-linecap="round" stroke-linejoin="round" fill="none" class="trace"/>'
 s+=circle(967,27,4,c['accent'],cls='pulse')
 s+='</svg>'; (A/f'footer-{theme}.svg').write_text(s)

def make_activity(theme, entries):
 c=colors[theme];s=svg_open(1200,238,'Recently updated public repositories','Dynamic preview of recently updated public projects fetched from the GitHub API.',c)
 s+=rect(1,1,1198,236,c['panel'],c['border'],16,2)
 s+=circle(36,39,5,c['a2'],cls='blink')+label(50,44,'RECENT PUBLIC WORK',c['ink'],18,'mono',700)
 s+=label(902,44,'UPDATED VIA GITHUB ACTIONS',c['faint'],11,'mono')
 # rows 3 columns
 for i,e in enumerate(entries[:3]):
  x=31+i*386;y=68
  s+=rect(x,y,366,144,c['bg'],c['border'],11)
  s+=label(x+19,y+27,('0'+str(i+1)+' / REPOSITORY'),c['faint'],11,'mono')
  name=e.get('name','public-project');name=name if len(name)<=27 else name[:24]+'...'
  s+=label(x+19,y+61,name,c['ink'],19,weight=710)
  description=(e.get('description') or 'Public source and experiments').replace('\n',' ')
  import textwrap
  words=textwrap.wrap(description,38)[:2]
  for j,l in enumerate(words):s+=label(x+19,y+86+j*17,l,c['muted'],12)
  # bottom subtle accent
  s+=rect(x+19,y+120,34,3,c['accent' if i==0 else 'a2' if i==1 else 'warm'],r=1)
 s+='</svg>'; (A/f'activity-{theme}.svg').write_text(s)

if __name__ == "__main__":
    for theme in colors:
        make_hero(theme)
        make_spikeproof(theme)
        make_footer(theme)
    examples = [
        {"name": "spikeproof-releases", "description": "Desktop installers and releases for Spikeproof."},
        {"name": "Similarity-Scout", "description": "TypeScript project exploring similarity."},
        {"name": "hunter.me", "description": "Personal website project in TypeScript."},
    ]
    for theme in colors:
        make_activity(theme, examples)
    print("Regenerated self-hosted SVG assets (activity in sample mode).")
