groups :: Int -> [a] -> [[a]]
groups n = map (take n) . takeWhile (not . null) . iterate (drop n)

removeEveryNth :: Int -> [a] -> [a]
removeEveryNth n = concatMap (take (n-1)) . groups n

rm :: Int -> [a] -> ([a], [a])
rm n x= (take (n-1) $ removeEveryNth n x, drop (n-1) $ removeEveryNth n x)                                                                                          

sieve :: Int -> [Int]
sieve len = (\(x,y) -> x ++ y) $
    last $
        takeWhile (\(y1, y2) -> (not . null) y2) $
            iterate (\(y1, y2) -> rm (head y2) (y1++y2)) ([1], [2..len])

main = (fmap sieve $ fmap (\x -> read x :: Int) getLine) >>= print
