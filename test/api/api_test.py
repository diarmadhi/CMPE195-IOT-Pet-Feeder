import requests

AWS_SERVER = 'http://ec2-13-57-38-126.us-west-1.compute.amazonaws.com:8000'
PET_FEEDERS = '/petfeeders/'
PET_FEEDER = '/petfeeders/1/'

TOKEN = '370d85a677fd646ef17cf6563a247e70f2d1ac25'

HEADERS = {
    'Authorization' : 'Token ' + TOKEN
}

class TestResult:
    def __init__(self, error = "", message = "", status_code=-1):
        self.error = error
        self.message = message
        self.status_code = status_code
        self.success = self.status_code in [200, 201, 202]

    def __str__(self):
        if self.success:
            return "\n".join(["Success", self.message, str(self.status_code)])
        return "\n".join(["Failed", self.message, self.error, str(self.status_code)])
            
    
    def __bool__(self):
        return self.success


def test_get(query):
    result = requests.get(query, headers=HEADERS)
    if result.status_code == 200:
        return TestResult("Success", result.text, result.status_code)
    return TestResult("Failed", result.text, result.status_code)
    

def test_put(query, params):
    result = requests.put(query, headers=HEADERS, data=params)
    if result.status_code == 200:
        return TestResult("Success", result.text, result.status_code)
    return TestResult("Failed", result.text, result.status_code)

def test_post(query, params):
    result = requests.post(query, headers=HEADERS, data=params)
    if result.status_code == 200:
        return TestResult("Success", result.text, result.status_code)
    return TestResult("Failed", result.text, result.status_code)


def main():
    # simple get
    if False:
        res = test_get(AWS_SERVER + PET_FEEDERS)
        if not res:
            print(res.error)
            print(res.message)
        else:
            print(res.message)

    # update pet food feeder
    if False:
        params = {
            "id": 1,
            "serial_id": "321",
            "setting_cup": 3,
            "setting_interval": 1,
            "setting_closure": False,
            "user": 1,
            "food": 1,
            "pet": 1
        }
        res = test_put(AWS_SERVER + PET_FEEDER, params)
        if not res:
            print(res.error)
            print(res.message)
        else:
            print(res.message)


    # account creation
    if False:
        params = {
            "username": "test",
            "password": "test",
        }
        res = test_post(AWS_SERVER + "/register/", params)
        if not res:
            print(res.error)
            print(res.message)
        else:
            print(res.message)

    # pet addition
    if True:
        params = {
            "chip_id" : "111",
            "pet_type" : "pettype",
            "pet_breed" : "breed2",
            "name" : "spot",
            "birthday" : "2016-01-01",
            "user" : "2"
        }
        res = test_post(AWS_SERVER + "/pets/", params)
        print(res)




if __name__ == '__main__':
    main()
