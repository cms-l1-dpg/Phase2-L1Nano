import uproot
import awkward as ak
import hist


forig = uproot.open("L1Ph2Nano_noMod100evts.root")
torig = forig["Events"]
f = uproot.open("L1Ph2Nano.root")
t = f["Events"]

new_branches = list(set(t.keys()) - set(torig.keys()))
new_branches.sort()
print("Additional Branches:", new_branches)

potential_arrays = ['L1Vertex_hwNTracksIn', 'L1Vertex_hwNTracksOut', 'L1Vertex_hwPt', 'L1Vertex_hwQual', 'L1Vertex_hwValid', 'L1Vertex_hwZ0', 'L1Vertex_sumPt', 'L1Vertex_z0']
arrs = t.arrays([b for b in potential_arrays if b in t.keys()])
print("L1Vertex fields:", arrs.fields)
#['L1Vertex_hwNTracksIn', 'L1Vertex_hwNTracksOut', 'L1Vertex_hwPt', 'L1Vertex_hwQual', 'L1Vertex_hwValid', 'L1Vertex_hwZ0', 'L1Vertex_sumPt', 'L1Vertex_z0']
assert ak.min(arrs.L1Vertex_hwValid) == 1 and ak.max(arrs.L1Vertex_hwValid) == 1, "hwValid bit is not giving the expected value of always 1"
assert ak.min(arrs.L1Vertex_hwPt) >= 0, "SumPt for vertices is less than zero"
assert ak.max(arrs.L1Vertex_hwPt) < 2**10, "(hw) SumPt for vertices exceeds the maximum specified in the interface doc"
if "L1Vertex_hwQual" in t.keys():
    assert ak.min(arrs.L1Vertex_hwQual) == ak.max(arrs.L1Vertex_hwQual), "hwQual has non-Zero value, update the test if this part of the word is now filled"
if "L1Vertex_hwNTracksIn" in t.keys():
    assert ak.min(arrs.L1Vertex_hwNTracksIn) == ak.max(arrs.L1Vertex_hwNTracksIn), "hwNTracksIn has non-Zero value, update the test if this part of the word is now filled"
if "L1Vertex_hwNTracksOut" in t.keys():
    assert ak.min(arrs.L1Vertex_hwNTracksOut) == ak.max(arrs.L1Vertex_hwNTracksOut), "hwNTracksIn has non-Zero value, update the test if this part of the word is now filled"
print("L1Vertex hwZ0 interpretation wrong, will need to fill with properly signed int")
# >>> ak.max(arrs.L1Vertex_hwZ0)
# 13
# >>> ak.min(arrs.L1Vertex_hwZ0)
# -2147483648
# >>> ak.min(arrs.L1Vertex_z0)
# -14.824219
# >>> ak.max(arrs.L1Vertex_z0)
# 13.880859
