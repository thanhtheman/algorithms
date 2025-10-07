# insortion sort

arr = [5,2,1,6,4,3]

for i in range(1,len(arr)):
    key = arr[i]
    j = i - 1
    while j >=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = key

print(arr)

''' 
Start with one number and compare it to the left number.
5 doesn't have the left number, so we can start at 2
because we will go one by one, so it must be a loop.
We start at 2, hence the range starts at 1, not 0
we will loop til the end of the array, hence the len(arr) is the last number which is 6
range(1,6) will give us index: 1,2,3,4,5, which correspond to arr[1] = 2, arr[2] =1...etc
--> for i in range (1, len(arr)):
as we will compare 2 numbers and swith their positions if a certain condition is met: the left number is greater than the current number.
we call the current number is "key" --> key = arr[i]
Next, the left number of key will be j, in term of position, j = i-1
Now, let's see 2 and 5, 5 > 2, so we will swith position. And that's it
[2, 5, 1, 6, 4, 3]

Moving forward, 

'''