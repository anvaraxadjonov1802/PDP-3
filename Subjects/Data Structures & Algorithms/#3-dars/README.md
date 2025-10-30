# 🧩 LeetCode #35 — Search Insert Position

## 📘 Description
Given a **sorted array of distinct integers** and a **target value**, return the **index** if the target is found.  
If not, return the index where it **should be inserted** in order.

You must write an algorithm with **O(log n)** runtime complexity.

---

## 🧠 Example

### Example 1
**Input:**
```python
nums = [1, 3, 5, 6]
target = 5
```
**Output:**
```
2
```

### Example 2
**Input:**
```python
nums = [1, 3, 5, 6]
target = 2
```
**Output:**
```
1
```

### Example 3
**Input:**
```python
nums = [1, 3, 5, 6]
target = 7
```
**Output:**
```
4
```

---

## ⚙️ Constraints
- 1 <= nums.length <= 10⁴  
- -10⁴ <= nums[i] <= 10⁴  
- All elements in `nums` are **distinct**  
- -10⁴ <= target <= 10⁴  

---

## 🚀 Approach
Since the array is **sorted**, we can use **Binary Search** to achieve `O(log n)` complexity:

1. Initialize two pointers: `left = 0` and `right = len(nums) - 1`.
2. While `left <= right`, find `mid = (left + right) // 2`.
3. If `nums[mid] == target` → return `mid`.
4. If `nums[mid] < target` → move `left = mid + 1`.
5. Else → move `right = mid - 1`.
6. If not found, return `left` (the correct insert position).

---

## 🧩 Code Implementation (Python)
```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
```

---

## 🧮 Time & Space Complexity
| Type | Complexity |
|------|-------------|
| Time | **O(log n)** |
| Space | **O(1)** |

---

## 🏁 Summary
✅ Uses **binary search**  
✅ Runs in **logarithmic time**  
✅ Handles edge cases (target smaller/larger than all elements)  

---

### 📂 File Info
- **Filename:** `solution.py`  
- **LeetCode Link:** [https://leetcode.com/problems/search-insert-position/](https://leetcode.com/problems/search-insert-position/)
