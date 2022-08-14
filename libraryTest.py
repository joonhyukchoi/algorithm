from collections import deque

q = deque()
q.append(2)
q.append(3)
q.popleft()
print('queue: ', q, q[0])

from itertools import permutations

permutation_list = [1, 2, 3, 4, 5]

for x in permutations(permutation_list, 2):
    print('permutation list: ', list(x) ,end = ' ')

from itertools import combinations

combination_list = [1, 2, 3, 4, 5]

for x in combinations(combination_list, 2):
    print('combination list: ', list(x), end = ' ')

import heapq

heap = []
heapq.heappush(heap, (1, 2))
heapq.heappush(heap, (2, 1))
heapq.heappop(heap)
print('heap: ', heap)

from collections import defaultdict

dict_type1 = defaultdict(list)
dict_type2 = defaultdict(set)

dict_type1['a'].append(1)
dict_type1['a'].append(2)
dict_type1['b']
print('list type dictionary: ', dict_type1)

dict_type2['a'].add(1)
dict_type2['a'].add(2)
temp_set = set([3, 4])
dict_type2['a'] = dict_type2['a'] | temp_set
print('set type dictionary: ', dict_type2)

#  문자열
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# import heapq
# def solution(A):
#     # write your code in Python 3.6
#     heap = []
#     count = 0
#     for el in A:
#         heapq.heappush(heap, (-el, el))
#         if len(heap) == heap[0][1]:
#             count += 1
#     return count


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     # write your code in Python 3.6
#     if len(A) <= 1:
#         return -2
#     min_distance = 100000001
#     A.sort()
#     for i in range(len(A) - 1):
#         min_distance = min(min_distance, A[i + 1] - A[i])
#     if min_distance == 100000001:
#         return -1
#     else:
#         return min_distance

#         package com.codility.tasks.hibernate.solution;

# import org.springframework.stereotype.Service;
# import org.springframework.data.jpa.repository.JpaRepository;
# import org.springframework.beans.factory.annotation.Autowired;

# import javax.persistence.Entity;
# import javax.persistence.EntityManager;
# import javax.persistence.Id;
# import javax.persistence.Table;
# import java.util.List;

# // 3번 문제는 자바 스프링을 사용해 본 경헝이 없어서 구글 서치를 통해 문제 풀이를 진행했음을 말씀드립니다.
# @Entity
# @Table(name = "person_data")
# class Person {
#     // 힌트에서 @Id 어노테이션으로 충분하다고 언급
#     @Id
#     @Column(name = "id", columnDefinition = "bigint")
#     private long id;

#     @Column(name = "first_name", columnDefinition = "varchar(255)")
#     private String first_name;

#     @Column(name = "last_name", columnDefinition = "varchar(255)")
#     private String last_name;

#     public String getFullName() {
#         return this.first_name + " " + this.last_name;
#     }
# }

# @Service
# class PersonService {
#     @PersistenceContext
#     private EntityManager em;

#     List<Person> findAll() {
#         String findPersonQuery = "SELECT * FROM person_data";  
#         List<Person> personList = em.createQuery(findPersonQuery, Person.class);
#         return personList;
#     }

# }



# -- write your code in PostgreSQL 9.4
# -- 4번 문제는 쿼리에서 기억안나는 부분(서브쿼리부분 + ..)들을 구글에서 서치하여 문제를 해결했습니다.
# -- testcase 2번 결과 Peter -> Kate로 수정 필요합니다.
# SELECT TP.name 
# FROM phones TP
# WHERE 10 <= (SELECT SUM(duration)
#             FROM calls
#             WHERE caller = TP.phone_number OR callee = TP.phone_number)
# ORDER BY TP.name ASC;
