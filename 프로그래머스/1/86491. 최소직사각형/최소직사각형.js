function solution(sizes) {
    let minSize = Math.min(sizes[0][0], sizes[0][1]);
    let maxSize = Math.max(sizes[0][0], sizes[0][1]);

    for(let i = 1; i < sizes.length; i++){
        let currentMin = Math.min(sizes[i][0], sizes[i][1]);
        let currentMax = Math.max(sizes[i][0], sizes[i][1]);

        if (currentMin > minSize)  minSize = currentMin;
        if (currentMax > maxSize)  maxSize = currentMax;
    }

    return minSize * maxSize;
}

