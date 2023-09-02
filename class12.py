def math1(first_num , opr , sec_num):
    match opr: 
        case "+":
            print(first_num + sec_num )
        case "-":
            print(first_num - sec_num)

        case "x" | "*":
            print(first_num * sec_num )

        case "/" :
            print(first_num / sec_num) 


math1(202, "+" ,400)
