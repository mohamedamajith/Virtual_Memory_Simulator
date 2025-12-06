# PAGE_SIZE = 1024   # 1 KB
# NUM_PAGES = 8
# NUM_FRAMES = 4

# class VirtualMemorySimulator:
#     def __init__(self):
#         self.page_table = [-1] * NUM_PAGES   # -1 means not loaded
#         self.frames = [None] * NUM_FRAMES    # store page numbers

#     def translate(self, logical_address):
#         page_num = logical_address // PAGE_SIZE
#         offset = logical_address % PAGE_SIZE

#         if page_num >= NUM_PAGES:
#             return None, page_num, None, "Invalid Logical Address"

#         frame_num = self.page_table[page_num]

#         # Page Fault
#         if frame_num == -1:
#             if None in self.frames:
#                 free_frame = self.frames.index(None)
#                 self.frames[free_frame] = page_num
#                 self.page_table[page_num] = free_frame
#                 page_fault = True
#                 frame_num = free_frame
#             else:
#                 return None, page_num, None, "No Free Frames"
#         else:
#             page_fault = False

#         physical_address = frame_num * PAGE_SIZE + offset
#         return physical_address, page_num, frame_num, page_fault


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


PAGE_SIZE = 1024   # 1 KB
NUM_PAGES = 8
NUM_FRAMES = 4

class VirtualMemorySimulator:
    def __init__(self):
        self.page_table = [-1] * NUM_PAGES   # -1 = not loaded
        self.frames = [None] * NUM_FRAMES    # None = empty frame

    def translate(self, logical_address):
        page_num = logical_address // PAGE_SIZE
        offset = logical_address % PAGE_SIZE

        if page_num >= NUM_PAGES:
            return None, page_num, None, "Invalid Logical Address"

        frame_num = self.page_table[page_num]

        # Page Fault
        if frame_num == -1:
            if None in self.frames:
                free_frame = self.frames.index(None)
                self.frames[free_frame] = page_num
                self.page_table[page_num] = free_frame
                page_fault = True
                frame_num = free_frame
            else:
                return None, page_num, None, "No Free Frames"
        else:
            page_fault = False

        physical_address = frame_num * PAGE_SIZE + offset
        return physical_address, page_num, frame_num, page_fault

