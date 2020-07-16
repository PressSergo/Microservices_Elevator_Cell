package Diplom.DefiantMessage.controller;

import Diplom.DefiantMessage.Services.Publisher;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class StandartElevator {

    @Autowired
    Publisher publisher;

    @GetMapping("/cellStandart")
    public void SendMessage(){
        publisher.SendCell();
    }
}
