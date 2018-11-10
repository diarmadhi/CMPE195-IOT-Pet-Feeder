#pragma once
#include <iostream>

//#include "json/json.hpp"
//
//using json = nlohmann::json;

class Response {
  public:
    Response() {}
    //virtual void response(json payload);
    void response(const std::string& payload) {
        std::cout << payload << std::endl;
    }
};
