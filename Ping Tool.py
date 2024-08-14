from ping3 import ping



# Defines the answers
loop_or_no_loop_answer_l = ["l", "L"]
loop_or_no_loop_answer_u = ["u", "U"]
loop_or_no_loop_answer_u_answer_y = ["y", "Y", "yes,", "Yes"]
loop_or_no_loop_answer_u_answer_n = ["n", "N", "no", "No"]

while True:
    # Ask the user for an IP address or domain
    address = input("""Please enter an IP address or domain:
    > """)

    # Ask the user if they want to loop the pings for a set amounts of times or until script is stopped
    loop_or_no_loop = input("""[l] = loop pings for a set amount of times:
[u] = loop pings until the script is stopped:
    > """)

    # Ask the user how many times to ping for
    if loop_or_no_loop in loop_or_no_loop_answer_l:
        loop_times = int(input("""How many times do you want to loop the pings:
    > """))
        while True:
            for i in range(loop_times):
                delay = ping(address)  # sends a single ping and returns the delay
                print(f"{address} pinged {i+1} times... {delay} ms")
            delay_average = delay + delay / i
            print(f"Average ms = {delay_average} ms")
            if delay is False:
                print(f"""
            Something has gone wrong :(
                    ERROR #00001
You are having trouble pinging {address}.""")
            
            elif delay is None:
                print(f"""
            Something has gone wrong :(
                    ERROR #00001
You are having trouble pinging {address}.""")
            break
        print("")



    elif loop_or_no_loop in loop_or_no_loop_answer_u:
        confirm = input("""[y] = yes [n] = no:
    > """)
        if confirm in loop_or_no_loop_answer_u_answer_y: 
            # Continuously ping the address
            i = 1
            while True:
                delay = ping(address)
                print(f"{address} pinged {i} times... {delay} ms")
                i += 1
                if delay is False:
                    print(f"""
            Something has gone wrong :(
                    ERROR #00001
You are having trouble pinging {address}.""")
                    break
                
                elif delay is None:
                    print(f"""
            Something has gone wrong :(
                    ERROR #00001
You are having trouble pinging {address}.""")
                    break

        print("")

        if confirm in loop_or_no_loop_answer_u_answer_n:
            print("")