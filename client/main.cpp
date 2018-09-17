#include "mqtt/client.h"

constexpr char TOPIC[] = "hello";
constexpr char PAYLOAD[] = "hello world";

constexpr char CLIENT_ID[] = "generic id";
constexpr char ADDRESS[] = "test.mosquitto.org";

int main() {
    


    mqtt::client cli(ADDRESS, CLIENT_ID);

    mqtt::connect_options connOpts;
    connOpts.set_keep_alive_interval(20);
    connOpts.set_clean_session(true);

    try {
        cli.connect(connOpts);
        auto msg = mqtt::make_message(TOPIC, PAYLOAD);
        cli.publish(msg);
        cli.disconnect();
    } catch (const mqtt::exception& e) {
        std::cerr << e.what() << std::endl;
    }

    
	return 0;
}
