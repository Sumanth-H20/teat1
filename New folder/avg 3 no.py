##avg of 3 numbers

#def calc_avg (a ,b ,c):
 #   sum = a+b+c
  #  avg = sum/3
   # print(avg)
    #return avg
#calc_avg (2,3,4)

#num = [1,2 ,3 , 4]
#def print_len(list):
  #  print(len(list))

#print_len(num)

#def print_list(list):
  #  for i in list:
     #   print(i , end = " ")

#print_list (num)


##find the factorial of n (n is the parameter)

#def calc_fact(n):
 #   fact = 1
  #  for i in range(1,n+1):
   #     fact*=i
   # print(fact)
#calc_fact(5)

## convert uds to inr

#def converter(usd_val):
   # inr_val =usd_val *83
  #  print (usd_val, "usd =" , inr_val,"inr")

#converter(10)

##factorial of n using recursion

#def fact(n):
 #   if(n==0 or n==1):
  #      return 1
   # return fact(n-1)*n
#print (fact(6))



##calculate the sum of first n natural numbers(using recursion)

#def calc_sum(n):
 #   if(n==0):
  #      return 0
   # return calc_sum(n-1)+n

#sum = calc_sum(5)
#print(sum)

##print all the elments of list using recursive function

#def print_list(list,i=0):
 #   if(i==len(list)):
  #      return
   # print (list[i])
    #print_list(list, i+1)


#num = [1,2,3,4,5]
#print_list(num)


## file i/o

