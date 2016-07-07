# Given a list representing stock prices (Index = minutes past trade opening time, Value = price of the stock), returns: The best profit possible from 1 purchase and 1 sale of this stock.
def maxProfit(stock_prices_yesterday):
    if len(stock_prices_yesterday)<2:
        raise("need at least 2 prices")
        
	min_Price=stock_prices_yesterday[0]
    maxProfit=stock_prices_yesterday[1]-min_Price
    
    for index, current_price in enumerate(stock_prices_yesterday):
        
        if index==0:
            continue
        potentialProfit=current_price-min_Price
        
        maxProfit=max(potentialProfit,maxProfit)
        
        min_Price=min(min_Price, current_price)
        
	return maxProfit


# Given a list of int, returns: A list of int with, for each index, the product of every integer except the integer of that index
def productSoFar(int_list):
    
    productOfAll=[None]*len(int_list)
    productSoFar=1
    i=0
    
    while i<len(int_list):
        productOfAll[i]=prodcutSoFar
        productSoFar*=int_list[i]
        i+=1
    
    productSoFar=1
    i=len(int_list-1)
    
    while i>=0:
        productOfAll[i]*=prodctSoFar
        productSoFar*=int_list[i]
        i-=1
        
        
    return productOfAll    



# Given a list of ints, returns: The highest possible product with 3 of the ints
def highest_product(list_of_ints):
    
        
    if len(list_of_ints) < 3:
        return IndexError("Not enough values to return the highest product of three")
    
    minimum = min(list_of_ints[0], list_of_ints[1])
    maximum = max(list_of_ints[0], list_of_ints[1])
    highest_of_two = list_of_ints[0] * list_of_ints[1]
    lowest_of_two = list_of_ints[0] * list_of_ints[1]
    highest_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    
    for int_value in list_of_ints[2:]:
        
        highest_of_three = max(highest_of_three, int_value * highest_of_two, int_value * lowest_of_two)
        highest_of_two = max(highest_of_two, maximum * int_value)
        lowest_of_two = min(lowest_of_two, minimum * int_value)
        minimum = min(minimum, int_value)
        maximum = max(maximum, int_value)
        
    return highest_of_three



# Given a list of meeting time ranges, returns: A list of condensed ranges. Basically a "tuple concatenator"
def condense_meeting(my_list):
    sorted_meetings=sorted(my_list)
    merged_meetings=[]
    
    previous_strat, previous_end=sorted_meetings[0]
    
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        if current_meetings_start<previous_meeting_end:
            previous_meeting_end=max(previous_meeting_end, current_meeting_end)
        else:
            merged_meetings.append(current_meeting_start,current_meeting_end)
            previous_meeting_start,previous_meeting_end=current_meeting_start,current_meeting_end
            
    merged_meetings.append(previous_meeting_start, previous_meeting_end)
    
    return merged_meetings



# Given an amount of money and a list of possible coins, returns: The number of different ways to make the amount with combinations of the coins
def make_amount(amount, denominations):
    
    numbers_of_ways = [0] * (amount + 1)
    numbers_of_ways[0] = 1
    
    for coin in denominations:
        
        for higher_amount in xrange(coin, amount + 1):
            higher_amount_remainder = coin - higher_amount
            
            numbers_of_ways[higher_amount] += numbers_of_ways[higher_amount_remainder]
            
            return numbers_of_ways[amount]



# Given a binary tree, returns: If the tree is a valid binary search tree
def is_BST(tree_root):
    
    nodes = []
    MINBOUND = - sys.maxint
    MAXBOUND = sys.maxint
    nodes.append(tree_root, MINBOUND, MAXBOUND)
    
    while len(nodes):
        
        node, minbound, maxbound = nodes.pop()
        
        if node < minbound or node > maxbound:
            return False
        
        if node.left:
            nodes.append(node.left, minbound, node.value)
            
        if node.right:
            nodes.append(node.right, node.value, maxbound)
            
    return True



# Given a "rotated" list, returns: The "rotation point" of that list. That is the point where the list starts at its "normal" point
def find_rotation_point(word_list):
    
    left_index = 0
    right_index = len(word_list) - 1
    
    while left_index < right_index:
        
        middle = ((right_index - left_index) / 2) + left_index
        
        if word_list[middle] > word_list[left_index]:
            left_index = middle
            
        else:
            right_index = middle
        
    return right_index + 1



# Given a list of movie lenghts and a flight duration, returns: If it is possible to watch two of this movies during the flight.
def two_movies(flight_lenght, movie_length):
    
    second_movie = {}
    
    for first_movie in movie_length:
        
        remaining_time = flight_lenght - first_movie
        
        if remaining_time in second_movie:
            return True
        
        else:
            second_movie[first_movie] = True
            
    return False



# Given a int, returns: The nth fibonacci number
def fib(n):
    
    if n < 0:
        raise Exception("Nique ta race")
        
    elif n < 2:
        return n
    
    previous_previous = 0
    previous = 1
    
    for i in range(n):
        
        current = previous_previous + previous
        previous_previous = previous
        previous = current
        
    return current



# Implementation of a Queue with 2 stacks
class myStack:
   def __init__ (self):
    self.instack[]
    self.outstack[]
        
        
    def enqueue (self, element):
        self.intsack.append(element)
        
        
    def dequeue (self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
            
         
         return self.outstack.pop()



# Implementation of a class with a function returning the largest element in the stack
class M_stack:
    def __init__ (self):
        self.stack=stack()
        self.maxstack=stack()
        
        def push(self,item):
            self.stack.push(item)
            if item>=self.maxstack.peek():
                self.maxstack.push(item)
        
        def pop (self,item):
            item=self.stack.pop()
            if (item==self.maxstack.peek()):
                self.maxstack.pop()
                
                    

            return item
    def max(self):
        return self.maxstack.peek()



# Given a list of many duplicate ints and one unique int, returns: The unique int
def find_unique_delivery_id(delivery_ids):
    
    xor_total = 0
    
    for ID in delivery_ids:
        
        xor_total ^= ID
        
    return xor_total



# Given a singly-linked list, returns: wheter the list has a cycle
def contains_a_cycle(linked_list_head):
    
    cycle_searcher = linked_list_head.next
    cycle_checker = linked_list_head
    
    while cycle_searcher.next != None and cycle_searcher != None:
        
        cycle_checker = cycle_checker.next
        cycle_searcher = cycle_searcher.next.next
            
        if cycle_searcher == cycle_checker :
            return True
        
    return False




# Given a linked-list, returns: A reversed version of the list
 def reverse_linked_list(linked_list_head):

    previous_node = None
    current_node = linked_list_head
    next_node = None
    
    while current_node:
        
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        
        
    return previous_node



# Given an int k and the head of a singly linked list, returns: The kth to last node
# The case where head_node.next is null is missing
def kth_to_last_node(k, head_node):
    
    stick_start = head_node
    stick_end = head_node
    
    for i in range(k):
        
        stick_end = stick_end.next
        
    while stick_end:
        
        stick_end = stick_end.next
        stick_start = stick_start.next
        
    return stick_start.value



# Given a string, returns: a reversed version of the string
def reverse_string(string_to_reverse):
    
    # Strings are immutable, we need to create a list containing the letters of the string
    string_list = list(string_to_reverse)
    
    # We go through the list in both way with two cursor, and switch the values everytime
    # Until we reach the middle
    
    left_cursor = 0
    right_cursor = len(string_list) - 1
    
    while left_cursor < right_cursor:
        
        string_list[left_cursor], string_list[right_cursor] = string_list[right_cursor], string_list[left_cursor]
        
        left_cursor += 1
        right_cursor -= 1
     
    return str(string_list)



# Given a string message, returns: A "reversed" version of the message, inversing the words but not the letters
def reverse_words(string_message):
    
    word_list = string_message.split()
    left_cursor = 0
    right_cursor = len(word_list) - 1
    
    while left_cursor < right_cursor:       
        word_list[left_cursor], word_list[right_cursor] = word_list[right_cursor], word_list[left_cursor]
        
        left_cursor += 1
        
        right_cursor -= 1
        
    return ' '.join(word_list)



# Given a string and the position of an opening parenthesis, returns: The position of the corresponding closing parenthesis
def find_corresponding_parenthesis(sentence, position_of_opening):
    
    left_parenthesis = 1
    right_parenthesis = 0
    
    for i in range(position_of_opening + 1, len(sentence) + 1):
        
        if sentence[i] == '(':
            
            left_parenthesis += 1
            
        if sentence[i] == ')':
            
            right_parenthesis += 1
            if left_parenthesis == right_parenthesis:
                return i



# Given a string, returns: If any permutation of this string can be a palindrome
def can_be_palindrome(input_string):
    
    char_parity = {}
    is_not_pair = 0
    
    for char in input_string:
        
        if char in char_parity:
            char_parity[charchar_parity] = {}
    is_not_pair = 0
    
    for char in input_string:
        
        if char in char_parity:
            char_parity[char] = not char_parity[char]
            
        else:
            char_parity[char] = False = not char_parity[char]
            
        else:
            char_parity[char] = False
    
    for parity in char_parity.itervalues():
        if parity == False:
            is_not_pair += 1
            
    return is_not_pair <= 1



# Given a string, returns: All possible permutations of this string, as a list
def get_permutations(input_string):
    
    if len(input_string) == 1 :
        return input_string
    
    new_permutations = []
    last_letter = input_string[-1]
    rest_of_word = input_string[: -1]
    previous_permutations = get_permutations(rest_of_word)    
    
    for previous_permutation in previous_permutations:
        
        for i in range(len(previous_permutation) + 1):
        
            new_permutation = previous_permutation[:i] + last_letter + previous_permutation[i:]
        
            if new_permutation not in new_permutations:
                new_permutations.append(new_permutation)
     
    return new_permutations



# Given a list of unsorted scores and a maximum possible score, returns: a sorted list. In O(n lg n) time
def fast_sort(unsorted_scores, highest_possible_score):
    
    scores_count = [0] * highest_possible_score
    sorted_scores = []
    
    for score in unsorted_scores:
        
        scores_count[score] += 1
        
    for score_value, score_occurence in enumerate(scores_count):
        
        for i in range(score_occurence):
            
            sorted_scores.append(score_value)
            
    return sorted_scores




# Given a list where every number appears once except for one which appears twice, returns: The number that appears twice
def unique(my_list):
    
    virtual = (len(my_list)-1) * ((len(my_list)-1) + 1)/2
    practical = 0
   
    for i in my_list:
        practical += i
        
    return practical - virtual



#
