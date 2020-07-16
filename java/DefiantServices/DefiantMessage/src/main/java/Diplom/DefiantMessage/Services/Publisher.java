package Diplom.DefiantMessage.Services;

import com.rabbitmq.client.Channel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;


@Service
public class Publisher {

    @Autowired
    Channel channel;

    public void SendCell() {
        try {
            channel.queueDeclare("Test",false, false, false, null);
        } catch (IOException e) {
            e.printStackTrace();
        }
        String message = "Hello World!";
        try {
            channel.basicPublish("", "Test", null, message.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(" [x] Sent '" + message + "'");
    }
}