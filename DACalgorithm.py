"""
Name: Connor Burke
Class: CS325 Spring 21
Assignment: Homework 2, #3 Divide and Conquer" 
"""

"""
code below is used from exploration: Divide-And-Conquer Algorithms
title: Merge Sort solution
Author: OSU coecs325 Instructor
4/10/21 available at https://replit.com/@coecs325/Merge-Sort
MajorityBirthdays replaced merge_sort to fit requirements for assignment
"""

def MajorityBirthdays(Arr,start,end):
    if(start<end):
        mid = (start+end)//2 #Computes floor of middle value
        MajorityBirthdays(Arr,start,mid)
        MajorityBirthdays(Arr,mid+1,end)
        merge(Arr,start, mid, end)

def merge(Arr, start, mid, end):
  #temporary arrays to copy the elements of subarray
  leftArray_size = (mid-start)+1
  rightArray_size = (end-mid)

  leftArray = [0]*leftArray_size
  rightArray = [0]*rightArray_size

  for i in range(0, leftArray_size):
    leftArray[i] = Arr[start+i]

  for i in range(0, rightArray_size):
    rightArray[i] = Arr[mid+1+i]

  i=0
  j=0
  k=start

  while (i < leftArray_size and j < rightArray_size):
    if (leftArray[i] < rightArray[j]):
      # filling the original array with the smaller element
      Arr[k] = leftArray[i]
      i = i+1
    else:
      # filling the original array with the smaller element
      Arr[k] = rightArray[j]
      j = j+1
    k = k+1

  # copying remaining elements if any
  while (i<leftArray_size):
    Arr[k] = leftArray[i]
    k = k+1
    i = i+1

  while (j<rightArray_size):
    Arr[k] = rightArray[j]
    k = k+1
    j = j+1


if __name__ == '__main__':
  Arr = [2,14,1,9,10,5,6,18,11]
  MajorityBirthdays(Arr, 0, 8)
  print(Arr)

  """
  end cited code from exploration: Divide-And-Conquer Algorithms
  """
