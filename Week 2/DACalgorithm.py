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
first if statement added to adjust code to work without mandatory start and end paramaters
"""

def MajorityBirthdays(Arr,start=None,end=None):
    if(start is None and end is None):
        start = 0
        end = len(Arr)
    if(start<end):
        mid = (start+end)//2 #Computes floor of middle value
        MajorityBirthdays(Arr,start,mid)
        MajorityBirthdays(Arr,mid+1,end)
        merge(Arr,start, mid, end)
        """
        end cited code from exploration: Divide-And-Conquer Algorithms
        """
        monday = 0
        tuesday = 0
        wednesday = 0
        thursday = 0
        friday = 0
        saturday = 0
        sunday = 0
        for i in range(len(Arr)):
            if (Arr[i]==1):
                monday = monday +1
            elif (Arr[i]==2):
                tuesday = tuesday +1
            elif (Arr[i]==3):
                wednesday = wednesday +1
            elif (Arr[i]==4):
                thursday = thursday +1
            elif (Arr[i]==5):
                friday = friday +1
            elif (Arr[i]==6):
                saturday = saturday +1
            elif (Arr[i]==7):
                sunday = sunday +1
        mostCommon = monday
        if(tuesday>mostCommon):
            mostCommon = tuesday
        if(wednesday>mostCommon):
            mostCommon = wednesday
        if(thursday>mostCommon):
            mostCommon = thursday
        if(friday>mostCommon):
            mostCommon = friday
        if(saturday>mostCommon):
            mostCommon = saturday
        if(sunday>mostCommon):
            mostCommon = sunday

        return mostCommon
        
"""
code below is used from exploration: Divide-And-Conquer Algorithms
title: Merge Sort solution
Author: OSU coecs325 Instructor
4/10/21 available at https://replit.com/@coecs325/Merge-Sort
"""
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
  """
  end cited code from exploration: Divide-And-Conquer Algorithms
  """
Arr = [4,3,6,1,2,3,6,5,4,3,2,1]
MajorityBirthdays(Arr)