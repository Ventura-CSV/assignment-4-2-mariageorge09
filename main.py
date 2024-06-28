def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    result.append(a1)
    result.append(a2)
    N = int(input('Enter the number of sequences: '))
    for num in range(2, N, 1):
        newres = (result[num-1]+ (result[num-2]) )
        result.append(newres)
        print (newres)
    print (result)
   
   

    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()
