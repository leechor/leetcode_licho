package main1
/**
全排列
 */
var r [][]int
var con = func(a []int, b int) bool {
	for _, aa := range a {
		if aa == b{
			return true
		}
	}
	return false
}

func permute(nums []int) [][]int {
	var tr []int
	backtrack(nums, tr)
	return r
}

func backtrack(nums []int, track []int) {
	if len(track) == len(nums) {
		z := make([]int, len(track), len(track))
		copy(z, track)
		r = append(r, z)
		return
	}

	for _, num := range nums {
		if con(track, num) {
			continue
		}

		track = append(track, num)
		backtrack(nums, track)
		track = track[:len(track)-1]
	}
}

func main() {
	a := []int{1, 2, 3, 4}
	r := permute(a)
	for _, rr := range r {
		for _, rrr := range rr {
			print(rrr)
		}
		println("")
	}
}
