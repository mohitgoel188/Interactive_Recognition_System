import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import pandas as pd
def api(url):
    '''Takes image url as input and return integer value corresponding 
        one of the following emotions:
        {'anger': 0, 
        'contempt': 1,  
        'disgust': 2, 
        'fear': 3, 
        'happiness': 4, 
        'neutral': 5, 
        'sadness': 6, 
        'surprise': 7 }'''
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '72defe188dec49299dc70f021c762fd6',
    }

    params = urllib.parse.urlencode({
    })
    body = "{ 'url': '"+url+"' }"

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        df=pd.read_json(data)
        dic=list(df['scores'])[0]
        result=sorted([(v,k) for k,v in dic.items()],reverse=True)[0]
        keys=list(dic.keys())
        for i in range(len(dic)):
            dic[keys[i]]=i;
        
        return dic[result[1]]
    except Exception as e:
        print(e.args)

def main():
    print(api('http://www.pick-health.com/wp-content/uploads/2013/08/happy-person.jpg'))
    
if __name__ == '__main__':
    main()