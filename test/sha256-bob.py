import pyEmp
import time

if __name__ == '__main__':
    emps = []
    for i in range(100):
        print(f"{i} preprocessing")
        time.sleep(0.1)
        e = pyEmp.EmpAg2pcGarbledCircuit("sha-256.txt", 2, "127.0.0.1", 12345, False)
        e.offline_computation()
        emps.append(e)

    for (i, e) in enumerate(emps):
        out = e.online_computation("fedc8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010")
        print("online computation finished")
        print(out)
        print(f"{i} press any key to continue")
        time.sleep(0.1)
        del e