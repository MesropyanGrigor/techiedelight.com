'''

Given a singly-linked list that stores a path formed by cells of a matrix, remove the redundant nodes in that path. The path can be both vertical and horizontal, but never diagonal. To determine the complete path, you need the endpoints of all vertical and horizontal paths; middle nodes don't provide any value and are therefore redundant. So, the resultant list should contain coordinates of only endpoints of all vertical and horizontal paths.

Input : (0, 1) → (0, 5) → (0, 8)
							↓
						  (2, 8)
							↓
						  (5, 8)
							↓
						  (7, 8) → (7, 10) → (7, 12) → None

Output: (0, 1) → (0, 8)
				   ↓
				 (7, 8) → (7, 12) → None

'''

class Solution:

	'''
	A singly-linked list node is defined as:

	class Node:
		def __init__(self, x=None, y=None, next=None):
			self.x = x			# x-coordinate
			self.y = y			# y-coordinate
			self.next = next	# pointer to the next node
	'''

	def removeNodes(self, head: Node) -> Node:
		if head is None:
			return None


		current = head.next
		prev = head
		
		nodes = [prev]
		check_by_x, check_by_y = current.x == prev.x, current.y == prev.y

		
		while current:
			if not check_by_x and not check_by_y:
				nodes.append(prev)
				prev = current
				current = current.next
				if current:
					check_by_x, check_by_y = current.x == prev.x, current.y == prev.y
					
				if check_by_x or check_by_y:
					nodes.append(prev)
				
				continue

			
			if check_by_x:
				if current.x != prev.x:
					nodes.append(prev)
					check_by_x, check_by_y = current.x == prev.x, current.y == prev.y
			elif check_by_y:
				if current.y != prev.y:
					nodes.append(prev)
					check_by_x, check_by_y = current.x == prev.x, current.y == prev.y

					
			prev = current
			current = current.next


		nodes.append(prev)
		for nn in range(len(nodes) - 1):
			nodes[nn].next = nodes[nn+1]
			
		
		return nodes[0]
			