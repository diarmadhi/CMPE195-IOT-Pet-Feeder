#include <iostream>
#include <unordered_map>

#include "mqtt/client.h"
#include "Response.h"

class Callback : public virtual mqtt::callback {

public:
    Callback(mqtt::client& cli) : cli_(cli) {}

    void connected(const std::string& cause) override {
        std::cout << "\nConnected: " << cause << std::endl;
        std::cout << std::endl;
    }

    // Callback for when the connection is lost.
    // This will initiate the attempt to manually reconnect.
    void connection_lost(const std::string& cause) override {
        std::cout << "\nConnection lost";
        if (!cause.empty())
            std::cout << ": " << cause << std::endl;
        std::cout << std::endl;
    }

    // Callback for when a message arrives.
    void message_arrived(mqtt::const_message_ptr msg) override {
        std::string topic(msg->get_topic());
        std::string payload(msg->get_payload_str());
        std::cout << topic << ": " << payload << std::endl;
        if (function_map_.find(topic) != function_map_.end()) {
            function_map_.at(topic).response(payload);
        } else {
            std::cout << "ERROR: Could not find function for topic: "
                << topic << std::endl;
        }
    }

    void delivery_complete(mqtt::delivery_token_ptr token) override {}

    bool add_function(const std::string& topic, const Response& function) {
        if (function_map_.find(topic) == function_map_.end()) {
            function_map_.insert(std::make_pair(topic, function));
            cli_.subscribe(topic);
            return true;
        }
        return false;
    }

private:
    std::unordered_map<std::string, Response> function_map_;
    mqtt::client& cli_;
};
