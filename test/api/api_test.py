import requests

AWS_SERVER = 'http://ec2-13-57-38-126.us-west-1.compute.amazonaws.com:8000/petfeeders/'
TOKEN = '370d85a677fd646ef17cf6563a247e70f2d1ac25'

HEADERS = {
    'Authorization' : 'Token ' + TOKEN
}

class TestResult:
    def __init__(self, success = False, error = "", message = ""):
        self.success = success
        self.error = error
        self.message = message
    
    def __bool__(self):
        return self.success


def test_get(query):
    result = requests.get(query, headers=HEADERS)
    if result.status_code == 200:
        return TestResult(True, "Success", result.text)
    return TestResult(False, "Failed", result.text)
    



def main():
    res = test_get(AWS_SERVER)
    if not res:
        print(res.error)
        print(res.message)
    else:
        print(res.message)




if __name__ == '__main__':
    main()
