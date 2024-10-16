
1. Input for Set A:

   • The program first prompts the user to input the number of elements they want to add to set A. This is done using int(input("number of a:")), where n will store this number.

   • An empty set a is created using a=set().

   • A loop runs n times, asking the user to input elements for set A. Each element is added to the set using a.add(element).

2. Input for Set B:

   • Similarly, the program asks for the number of elements for set B using int(input("number of b: ")), storing this in m.

   • An empty set b is created.

   • A loop runs m times, allowing the user to input elements for set B, which are added to the set in the same manner as before.

3. Set Operations:

   • The program calculates the union of sets A and B using a.union(b). The union includes all unique elements from both sets.

   • It also calculates the intersection of sets A and B using a.intersection(b), which includes only the elements that are present in both sets.

4. Output:

   • Finally, the program prints out:

     • The contents of set A.

     • The contents of set B.

     • The union of both sets.

     • The intersection of both sets.

This code effectively demonstrates basic set operations in Python, allowing users to explore how sets can be combined and compared.
