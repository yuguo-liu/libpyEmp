import pyEmp
import time
import gc

if __name__=='__main__':
    party, port = 2, 12345
    print("I'm Bob!")
    seed = 0x6ce5e3e490c21aac770a02077e050cebafe4bee76880f4a39590647f96778173
    m = 0x4ef9c1d8971dd47c63ac6e427536d1e34dcfe4fbe77d2d6118864009f42c96d243726536113ac1b7c977166154aaa44f

    str_seed = hex(seed)[2:]
    str_seed = "0" * (64 - len(str_seed)) + str_seed

    str_m = hex(m)[2:]
    str_m = "0" * (96 - len(str_m)) + str_m

    host = "127.0.0.1"

    ports = [12345 + i * 5 for i in range(10)]

    for i in range(10):
        s_time = time.time()
        tls_prf_96 = pyEmp.EmpTlsPrfSF(party, host, ports[i], "server finished", False)
        tls_prf_96.offline_computation()
        print(f"offline duration: {(time.time() - s_time) * 1000}ms")

        s_time = time.time()
        res = tls_prf_96.online_computation(str_seed, str_m)
        print(f"online duration: {(time.time() - s_time) * 1000}ms")

        print(f"0x{res}")
        input(f"{i} press any key to continue")
        del tls_prf_96