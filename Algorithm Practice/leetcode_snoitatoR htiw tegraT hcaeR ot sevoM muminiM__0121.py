class block:
    def __init__(self, state, loc, n):
        # state: snake's pose (R, D for now)
        # loc: head's current location
        # n: step count
        self.state=state
        self.loc=loc
        self.step=n
    def __str__(self):
        return f"[{self.loc} | {self.state} | {self.step}]"
    def __eq__(self, blk):
        print(f"lefthand side: {self.step}, {self.loc} &righthand side: {blk.step}, {blk.loc}") # self -> to add
        print(isinstance(blk, block) , blk.state == self.state , blk.loc[0] == self.loc[0] , blk.loc[1] == self.loc[1], blk.step >= self.step)
        return isinstance(blk, block) and blk.state == self.state and blk.loc == self.loc and blk.step >= self.step # 좌표는 같은데step수가 더 크면 제외하겠다는 말.
    
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        self.grid=grid
        self.record_R=[[-1 for _ in range(len(grid))] for _ in range(len(grid))]
        self.record_D=[[-1 for _ in range(len(grid))] for _ in range(len(grid))]
        min_path=-1
        # start from (0, 0) finish at (n-1, n-1)
        # Use stack
        # push all available moves
        stack = []
        stack.append(block("R" ,[0, 1], 0))
        
        # use current indicator
        # given current location and position
        # returns posible moves
        # with this result push to stack and
        # move record this enable
        while len(stack)>0:
            cur_blk=stack.pop()
            if cur_blk.state=="R":
                record=self.record_R
            else:
                record=self.record_D
            if record[cur_blk.loc[0]][cur_blk.loc[1]]==-1 or record[cur_blk.loc[0]][cur_blk.loc[1]]>cur_blk.step:
                record[cur_blk.loc[0]][cur_blk.loc[1]]=cur_blk.step
            # print("====")
            # print(cur_blk)
            # print(len(stack))
            if min_path!=-1 and cur_blk.step>=min_path:
                continue
            elif cur_blk.loc[0]==(len(grid)-1) and cur_blk.loc[1]==(len(grid)-1):
                if cur_blk.state=="R" and (min_path==-1 or cur_blk.step<min_path):
                    min_path=cur_blk.step
                    # print(min_path)
            
            toadd=self.availableMoves(cur_blk)
            # stack+=toadd
            # print(f"TOADD:{len(toadd)}")
            for b in toadd:
                if b.state=="R":
                    record=self.record_R
                else:
                    record=self.record_D
                # print(b, record[b.loc[0]][b.loc[1]])
                if b.step < record[b.loc[0]][b.loc[1]] or record[b.loc[0]][b.loc[1]]==-1:
                    stack.append(b)

        return min_path
    
    def availableMoves(self, blk):
        coor_0=blk.loc[0]
        coor_1=blk.loc[1]
        step=blk.step
        lst = []
        if blk.state=="R":
            if (coor_1+1)<=(len(self.grid)-1) and self.grid[coor_0][coor_1+1]==0: # going right
                lst.append(block("R", [coor_0, coor_1+1], step+1))
            if (coor_0+1)<=(len(self.grid)-1) and self.grid[coor_0+1][coor_1]==0 and self.grid[coor_0+1][coor_1-1]==0: # moving down and rotate to clock-wise
                lst.append(block("R", [coor_0+1, coor_1], step+1)) # moving down
                lst.append(block("D", [coor_0+1, coor_1-1], step+1)) # rotate to clock-wise
        else: # "D for now"
            if (coor_0+1)<=len(self.grid)-1 and self.grid[coor_0+1][coor_1]==0: #move down
                lst.append(block("D", [coor_0+1, coor_1], step+1))
            if (coor_1+1)<=(len(self.grid)-1) and self.grid[coor_0][coor_1+1]==0 and self.grid[coor_0-1][coor_1+1]==0: # move right or rotate to counter-clock-wise
                lst.append(block("D", [coor_0, coor_1+1], step+1)) # moving right
                lst.append(block("R", [coor_0-1, coor_1+1], step+1)) # rotate to counter-clock-wise
        return lst
