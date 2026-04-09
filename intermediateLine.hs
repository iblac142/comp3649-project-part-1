--tokenizing
data Tag = Operation
    | Literal
    | Variable
    | Temp
    | Error
    | Empty deriving Show


data Token a b = Token {
    tag   :: Tag, 
    value :: b
} deriving Show

test = Token Temp '1'
--tag test
--value test

--intermediateLine
data IntermediateLine a b c d = IntermediateLine {
    dst  :: a,
    src1 :: b,
    op   :: c,
    src2 :: d
} deriving Show

test1 = IntermediateLine test test test test

--Access: tag (dst (test1))