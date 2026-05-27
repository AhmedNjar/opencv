import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def plot_spindle_schematic(vars_dict):
    # 1. استخراج الأبعاد من القاموس
    L1, L2, L3, L4 = vars_dict['L1'], vars_dict['L2'], vars_dict['L3'], vars_dict['L4']
    R1, R2, R3, R4 = vars_dict['R1'], vars_dict['R2'], vars_dict['R3'], vars_dict['R4']
    ri = vars_dict['ri']
    
    # حساب مواقع الـ Z التراكمية
    z0 = 0
    z1 = L1
    z2 = z1 + L2
    z3 = z2 + L3
    z4 = z3 + L4
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # 2. رسم جسم السبيندل (أعلى وأسفل المحور)
    sections = [
        (z0, z1, R1), (z1, z2, R2), (z2, z3, R3), (z3, z4, R4)
    ]
    
    for start, end, R in sections:
        # الجزء العلوي
        ax.add_patch(patches.Rectangle((start, ri), end-start, R-ri, 
                                     facecolor='lightgrey', edgecolor='black', alpha=0.8))
        # الجزء السفلي (انعكاس)
        ax.add_patch(patches.Rectangle((start, -R), end-start, R-ri, 
                                     facecolor='lightgrey', edgecolor='black', alpha=0.8))

    # 3. رسم الثقب الداخلي (Bore)
    ax.axhline(y=ri, color='black', linestyle='--', linewidth=0.8)
    ax.axhline(y=-ri, color='black', linestyle='--', linewidth=0.8)
    ax.axhline(y=0, color='red', linestyle='-.', linewidth=1, label="Centerline")

    # 4. تحديد أماكن المحامل (Bearings)
    z_front = z1 + vars_dict['front_z_fraction'] * L2
    z_rear = z1 + vars_dict['rear_z_fraction'] * L2
    
    bearing_locs = [z_front, z_rear]
    for bz in bearing_locs:
        # رسم المحمل كمستطيل صغير مائل (Cross-hatched)
        ax.add_patch(patches.Rectangle((bz-5, R2+2), 10, 10, facecolor='orange', edgecolor='black', hatch='///'))
        ax.add_patch(patches.Rectangle((bz-5, -R2-12), 10, 10, facecolor='orange', edgecolor='black', hatch='///'))
        ax.text(bz, R2+15, 'Bearing', ha='center', fontsize=9, fontweight='bold')

    # 5. رسم القوى (Forces) عند الأنف (Nose)
    # Fr (Radial)
    ax.annotate('', xy=(z0, R1), xytext=(z0, R1+30),
                arrowprops=dict(facecolor='red', shrink=0.05, width=2))
    ax.text(z0-5, R1+35, f"Fr={vars_dict['Fr']}N", color='red', fontweight='bold')
    
    # Ff (Axial)
    ax.annotate('', xy=(z0, 0), xytext=(z0-40, 0),
                arrowprops=dict(facecolor='blue', shrink=0.05, width=2))
    ax.text(z0-60, 5, f"Ff={vars_dict['Ff']}N", color='blue', fontweight='bold')

    # 6. إضافة خطوط الأبعاد (Dimensions)
    def add_dim(x_start, x_end, y_level, text):
        ax.annotate('', xy=(x_start, y_level), xytext=(x_end, y_level),
                    arrowprops=dict(arrowstyle='<->', color='black'))
        ax.text((x_start+x_end)/2, y_level+2, text, ha='center', fontsize=9)

    add_dim(z0, z1, -R3-20, f"L1={L1}")
    add_dim(z1, z2, -R3-20, f"L2={L2}")
    add_dim(z2, z3, -R3-20, f"L3={L3}")
    add_dim(z4, z3, -R3-20, f"L4={L4}")
    
    # أقطار (Radii)
    ax.text(z1-L1/2, ri/2, f"ri={ri}", va='center', ha='center', fontsize=8, color='darkgreen')

    # إعدادات الرسم
    ax.set_xlim(z0-80, z4+50)
    ax.set_ylim(-R3-50, R3+60)
    ax.set_aspect('equal')
    ax.set_title("Geometric Configuration & Loads", fontsize=14, pad=20)
    ax.set_xlabel("Z-axis (Length mm)")
    ax.set_ylabel("R-axis (Radius mm)")
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    plt.show()

# مثال للتشغيل ببيانات من مشروعك
sample_vars = {
    "L1": 122.0, "L2": 405.0, "L3": 24.0, "L4": 15.0,
    "R1": 45.0, "R2": 50.0, "R3": 82.5, "R4": 45.0, "ri": 30.0,
    "front_z_fraction": 0.25, "rear_z_fraction": 0.75,
    "Fr": 500, "Ff": 300
}

plot_spindle_schematic(sample_vars)