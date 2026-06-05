class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        preference = {0: 0, 1: 0}
        c = 0
        for i in students:
            preference[i] = preference[i] + 1

        for i in sandwiches:
            if preference[i] > 0:
                preference[i] = preference[i] - 1
            else:
                return preference[0] + preference[1]
        return 0
                

