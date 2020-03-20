func firstDuplicate(a: [Int]) -> Int {
    var index = -1
    for i in 0..<a.count - 1 {
        for j in i+1..<a.count {
            if a[i] == a[j] {
                print("Found duplicate \(a[i])")
                if index == -1 || index > i {
                    print("Update index \(index) to \(i)")
                    index = i
                }
            } 
        }
    }
    return index
}

print("[2, 1, 3, 5, 3, 2]")
print(firstDuplicate(a: [2, 1, 3, 5, 3, 2]))
print("[2, 2]")
print(firstDuplicate(a: [2, 2]))
print("[2, 4, 3, 5, 1]")
print(firstDuplicate(a: [2, 4, 3, 5, 1]))