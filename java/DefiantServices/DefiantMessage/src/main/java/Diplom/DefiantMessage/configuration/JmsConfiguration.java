package Diplom.DefiantMessage.configuration;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

@Configuration
public class JmsConfiguration {

    @Bean
    ConnectionFactory getConnectionFactory() {
        ConnectionFactory connectionFactory = new ConnectionFactory();
        connectionFactory.setUsername("guest");
        connectionFactory.setPassword("guest");
        connectionFactory.setPort(5672);
        connectionFactory.setVirtualHost("/");
        connectionFactory.setHost("message_brocker");
        return connectionFactory;
    }

    @Bean
    Connection getConnection(){
        try {
            return getConnectionFactory().newConnection();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (TimeoutException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Bean
    Channel getChannel(){
        try {
            return getConnection().createChannel();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
