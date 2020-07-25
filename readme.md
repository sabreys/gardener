# Gardener 

 Gardener is basic mongodb mail-pass data searcher.You can load your user datas and fastly search in it. Nosql is  giving huge advantage for  big datas.you can transfer your sql datas to mongodb with this.there is a normalizer in it. I will add a sql formatter too. 
 
 
 ![enter image description here](https://github.com/sabreys/gardener/blob/master/screen.PNG?raw=true)


# Data File Example

     mail1@abc.com;pass1
     mail2@abc.com;pass2

## Features that I will add soon

  Pipe command : You can iterate over a query and  run your own function.

      def do_magic(function_name,query_filter):
example function:

      
      def send_mail(mail,pass):
        #sending mail with smtplib
        fromaddr = 'user_me@gmail.com'
        toaddrs  = mail
        msg = 'Please change your password for security. old password : {pass}'
        username = 'user_me@gmail.com'
        password = 'pwd'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()


        

        





