import base64,re,os
src=open('src.html',encoding='utf-8').read()
mime={'jpg':'image/jpeg','png':'image/png','mp4':'video/mp4'}
def rep(m):
    p=m.group(1); ext=p.rsplit('.',1)[1]
    return 'data:%s;base64,%s'%(mime[ext],base64.b64encode(open(p,'rb').read()).decode())
out=re.sub(r'(assets/[\w\-]+\.(?:jpg|png|mp4))',rep,src)
open('Electrodeposicion_NiCr.html','w',encoding='utf-8').write(out)
print(len(out)//1024,'KB')
