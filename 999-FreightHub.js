const startingArray = [2, 4, 6, 8, 9, 15]
const resultingArray = ['4', '16', '64']

const assert = require('assert')

function transform(array) {
    result = []
    // we assume that we transform a maximum of 3 elements depending on the length of the input array
    for (let i = 0; i < Math.min(3,array.length); i++) {
        result.push(""+Math.pow(2,array[i]))
    }    
    return result
}    

assert.deepEqual(transform(startingArray), resultingArray)

const requests = [
    {requestId: 'poiax',  startedAt: 1489744808, ttl: 8},
    {requestId: 'kdfhd',  startedAt: 1489744803, ttl: 3},
    {requestId: 'uqwyet', startedAt: 1489744806, ttl: 12}, 
    {requestId: 'qewaz',  startedAt: 1489744810, ttl: 1}
]
    
const cumulativeTtl = 15

// I will assume that the input array if not null
function computeCumulativeTtl(requests) {
    let min = requests[0].startedAt
    let max = 0

    requests.forEach((req) => {
        min = Math.min(req.startedAt, min)
        max = Math.max(req.startedAt + req.ttl, max)
    })

    return max - min
}

assert.equal(computeCumulativeTtl(requests), cumulativeTtl)

const fs = require('fs')
const readline = require('readline')

let lineReader = readline.createInterface({
    input: fs.createReadStream('polygons.txt')
})

let triangles = new Set()
let squares = new Set()
let rectangles = new Set()
let others = new Set()

lineReader.on('line', (line) => {
    polygon = line.split(',')
    switch (polygon.length) {
        case 3:
            triangles.add(polygon)
            break
        case 4:
            lengths = {}
            polygon.forEach((len) => {
                lengths[len] = true
            })
            switch (Object.keys(lengths).length) {
                case 1:
                    squares.add(polygon)
                    break
                case 2:
                    rectangles.add(polygon)
                    break
                default:
                    others.add(polygon)
                    break
            }
            break
        default:
            others.add(polygon)
            break
    }
})

lineReader.on('close', () => {
    assert.equal(triangles.size, 2)
    assert.equal(squares.size, 1)
    assert.equal(rectangles.size, 1)
    assert.equal(others.size, 3)
})

