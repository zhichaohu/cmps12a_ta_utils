from shutil import copyfile
import os

# IMPORTANT: any type of deletion/remove file/folder is prohibited in this script! If you need to delete anything,
# go to Terminal and do it yourself!

# Copies student submissions from "from_dir" to "to_dir". Student submission only contains file with name
# "file_name", each submission in its own folder. If student's CruzID is "zhu", folder name is, e.g.,
# "w14_zhu". If late submission, "w14_zhu_spec".


def copy_lab_one_folder(class_dir, quarter_folder, to_dir, lab_name, file_name):
    if "bin/moss" not in to_dir:
        return
    from_dir = os.path.join(class_dir, quarter_folder, lab_name)
    if not os.path.exists(from_dir):
        print("Warning! Previous submission folder does not exit!" + from_dir)
        return
    for student_folder in os.listdir(from_dir):
        from_student_dir = os.path.join(from_dir, student_folder)
        if not os.path.isdir(from_student_dir):
            continue
        to_student_dir = os.path.join(to_dir, quarter_folder.split(".")[1] + "_" + student_folder)
        if os.path.exists(to_student_dir):
            continue

        for name in file_name:
            submission_file = os.path.join(from_student_dir, name)
            if os.path.isfile(submission_file):
                os.mkdir(to_student_dir)
                copyfile(submission_file, os.path.join(to_student_dir, file_name[0]))
                break

        if not os.path.exists(to_student_dir):
            print("Warning! " + file_name[0] + " does not exist in: " + from_student_dir + " [Actual files: " +
                  ",".join(os.listdir(from_student_dir)) + "]")
            continue


if __name__ == "__main__":
    g_current_folder_name = "cmps012a-pt.w18"
    g_previous_folder_names = [
        "cmps011-pt.w14",
        "cmps011-pt.w15",
        "cmps011-pt.s15",
        "cmps011-pt.w16",
        "cmps011-pt.s17",
        "cmps012a-pt.w13",
        "cmps012a-pt.s14",
        "cmps012a-pt.f15",
        "cmps012a-pt.w16",
        "cmps012a-pt.w17"
    ]

    g_class_dir = "/afs/cats.ucsc.edu/class"
    g_submissions_previous_dir = "/afs/cats.ucsc.edu/class/cmps012a-pt.w18/bin/moss/submissions_previous"
    g_submissions_current_dir = "/afs/cats.ucsc.edu/class/cmps012a-pt.w18/bin/moss/submissions_current"

    g_lab_name = "pa5"
    # All possible names for late submission folders.
    g_special_lab_name = ["spec_" + g_lab_name, g_lab_name + "-spec", g_lab_name + "_spec", "s" + g_lab_name,
                          "spec-" + g_lab_name]
    # All possible names for submission files.
    g_file_name = ["Queens.java", "queens.java", "Queen.java", "queen.java"]

    g_to_dir_previous = os.path.join(g_submissions_previous_dir, g_lab_name)
    if os.path.exists(g_to_dir_previous):
        print("Path exit! Please delete first! " + g_to_dir_previous)
        exit()
    os.mkdir(g_to_dir_previous)
    for p in g_previous_folder_names:
        copy_lab_one_folder(g_class_dir, p, g_to_dir_previous, g_lab_name, g_file_name)
        for spec_lab in g_special_lab_name:
            copy_lab_one_folder(g_class_dir, p, g_to_dir_previous, spec_lab, g_file_name)

    g_to_dir_current = os.path.join(g_submissions_current_dir, g_lab_name)
    if os.path.exists(g_to_dir_current):
        print("Path exit! Please delete first! " + g_to_dir_current)
        exit()
    os.mkdir(g_to_dir_current)
    copy_lab_one_folder(g_class_dir, g_current_folder_name, g_to_dir_current, g_lab_name, g_file_name)
    for spec_lab_current in g_special_lab_name:
        copy_lab_one_folder(g_class_dir, g_current_folder_name, g_to_dir_current, spec_lab_current, g_file_name)

