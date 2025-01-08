from func_handcalcs import compressive_strength

def test_compressive_strength():
    latex_out_1, comp_strength_1 = compressive_strength(a = 100, b = 500, fy = 355)
    comp_strength_1 == 17750000.0

    latex_out_2, comp_strength_2 = compressive_strength(100000, 1, 1, 355)
    comp_strength_2 == 35.5e6