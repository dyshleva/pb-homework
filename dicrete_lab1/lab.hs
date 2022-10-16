import Data.List (nub)

filterBy :: Eq b => b -> (a -> b) -> [a] -> [a]
filterBy key fn = filter (((==) key) . fn)

combine :: Eq b => [(a, b)] -> [(b, c)] -> [([a], [c])]
combine abPairs bcPairs = 
    map 
    (\x -> (map fst (filterBy x snd abPairs), map snd (filterBy x fst bcPairs)))
    (nub $ map snd abPairs)

compose :: Eq b => [(a, b)] -> [(b, c)] -> [(a, c)]
compose lst_fst lst_snd =
    concat $
        map (\x -> [(a,b) | a <- fst x, b <- snd x]) $
            combine lst_fst lst_snd

main :: IO ()
-- main = print $ compose $ combine [(x,x+1) | x <- [1..7]] [(x, x+1) | x <- [3..8]]
main = print $ compose [(1, 1)] [(2, 2), (1, 1)]
