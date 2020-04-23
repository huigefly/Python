

// 在onCreate()中开启线程

new Thread(new GameThread()).start();
// 实例化一个handler

Handler myHandler = new Handler() {

 //接收到消息后处理

 public void handleMessage(Message msg) {

  switch (msg.what) {

  case Activity01.REFRESH:

   mGameView.invalidate();//刷新界面

   break;

  }

  super.handleMessage(msg);

 }                  

};
class GameThread implements Runnable {

 public void run() {

     while (!Thread.currentThread().isInterrupted()) {

         Message message = new Message();

            message.what = Activity01.REFRESH;

            //发送消息

            Activity01.this.myHandler.sendMessage(message);

            try {

             Thread.sleep(100);

            }

            catch (InterruptedException e) {

             Thread.currentThread().interrupt();

            }

  }

 }

}

