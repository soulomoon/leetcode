import scala.language.postfixOps

object Solution {
  def threeSum(nums: Array[Int]): List[List[Int]] = {
     if (nums.length < 3) {
      return List()
    }
   
    val num = nums.sorted
    val r = scala.collection.mutable.Set[List[Int]]()
    for (i <- num.indices.slice(0, num.length - 2)) {
      if (i < 1 || num(i) != num(i - 1)) {
        val d = scala.collection.mutable.Set[Int]()
        for (x <- num.slice(i + 1, num.length)) {
          if (!d.contains(x)) {
            d.add(-num(i) - x)
          } else {
            r.add(List(num(i), -num(i) - x, x))
          }
        }
      }
    }
    r.toList
  }

  def main(args: Array[String]): Unit = {
    val a = Array(-1, 0, 1, 2, -1, -4)
    val startTimeMillis = System.currentTimeMillis()
    println(Solution.threeSum(a))
    val endTimeMillis = System.currentTimeMillis()
    val durationSeconds = endTimeMillis - startTimeMillis
    println(durationSeconds)
  }
}

