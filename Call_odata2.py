import sys, requests, json, base64, time
import itertools
import threading
import time

done = False
#here is the animation
def animate():
    #for c in itertools.cycle(['|', '/', '-', '\\']):
    time.sleep(0.2)
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rWorking ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

def main(argv):
    url = ""
    dict1_ = {}
    try:
        if argv[0] == 'S':
            print( "Llamando SANTANDER..." )
            url = "https://l251118-iflmap.hcisbp.us3.hana.ondemand.com/http/rest/sftp/santander/readReceiptRespConf"
            #url = "https://e250562-iflmap.hcisbt.us3.hana.ondemand.com/http/rest/sftp/santander/readReceiptRespConf"
        elif argv[0] == 'H':
            print( "Llamando HSBC..." )
            #url = "https://e250562-iflmap.hcisbt.us3.hana.ondemand.com/http/rest/sftp/hsbc/readReceiptRespConf"
            url = "https://l251118-iflmap.hcisbp.us3.hana.ondemand.com/http/rest/sftp/hsbc/readReceiptRespConf"
        elif argv[0] == 'B':
            print( "Llamando BANORTE..." )    
            #url = "https://e250562-iflmap.hcisbt.us3.hana.ondemand.com/http/rest/sftp/banorte/readReceiptRespConf"
            url = "https://l251118-iflmap.hcisbp.us3.hana.ondemand.com/http/rest/sftp/banorte/readReceiptRespConf"
        else:
            print( f'Opción no definida {argv[0]}' )
    except IndexError as error:
        print('Opción necesarias[S/H/B]')   
        
    if url != "":
        r = requests.get( url , auth=('S0020939499', 'faltamiTRAXION2019'))
        #r = requests.get( url )
        print( r.status_code )
        #print( r.headers['content-type'] )
        #print( r.json() )
        output = r.json()
        print('Cantidad de archivos:', len(output))
        
#        for i, item in enumerate(output):
#            dict1_ = {k:v for (k,v) in item.items() if k == 'filename' if v.endswith( '.PDF' ) }
#            #dict1_ = {k:v for (k,v) in item.items()}
#            for key in dict1_:
#                #print(f'key type = {type(key)}')
#                print('{0}->{1}'.format(i,item[key]))
                
if __name__ == '__main__':
    start = time.time()
    t = threading.Thread(target=animate)
    t.start()
    main(sys.argv[1:])
    done = True
    end = time.time()
    elapsed = end - start
    
    sec, msec = divmod(elapsed, 60)
    mon, sec = divmod(elapsed, 60)
    hr, mon = divmod(mon, 60)
    print("time : %d:%02d:%02d" % (hr, mon, sec))

    #https://httpbin.org/post
    #curl -X GET " " -H "accept: image/jpeg"
    #curl -X GET "https://httpbin.org/basic-auth/gago/papo" -H "accept: application/json"