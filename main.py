import json
from Validator import Validator
from CopyPaste import CopyPaste

if __name__ == '__main__':
    json_file = open('Config.json')
    json_data = json.load(json_file)
# --- Copy AOI ---
    obj_validator_des = Validator(json_data['Path'][0]['Destination'])
    if obj_validator_des.valid_path():
        print(f"[Destination][{obj_validator_des.valid_path()}]    - {json_data['Path'][0]['Destination']}")
    else:
        exit()
    obj_validator_scr = Validator(json_data['Path'][0]['Source'])
    if obj_validator_scr.valid_path():
        print(f"[Source     ][{obj_validator_scr.valid_path()}]    - {json_data['Path'][0]['Source']}")
    else:
        exit()
    print(f"[Destination][year]    - {obj_validator_des.tree_of_dir_year()}")
    print(f"[Source     ][year]    - {obj_validator_scr.tree_of_dir_year()}")

    for year in obj_validator_scr.tree_of_dir_year():
        if year in obj_validator_des.tree_of_dir_year():
            print(f"[Destination][month]   - {obj_validator_des.tree_of_dir_month(str(year))}")
            print(f"[Source     ][month]   - {obj_validator_scr.tree_of_dir_month(str(year))[-2:]}")

            for month in obj_validator_scr.tree_of_dir_month(str(year))[-2:]:  # TODO [-2:]
                if month in obj_validator_des.tree_of_dir_month(str(year)):
                    if len(obj_validator_des.tree_of_dir_day(str(year),
                                                             str(month))) < \
                            len(obj_validator_scr.tree_of_dir_day(str(year),
                                                                  str(month))):
                        print(f"[Destination][day]     - Missing day in {month} month:")
                        for day in obj_validator_scr.tree_of_dir_day(str(year), str(month)):
                            if day not in obj_validator_des.tree_of_dir_day(str(year), str(month)):
                                print(f"                          day: {day}. Coping dir...")
                                obj_copy_paste = CopyPaste(str(obj_validator_des.path_month),
                                                           str(obj_validator_scr.path_month))
                                obj_copy_paste.copy_dir(str(day))
                            else:
                                if len(obj_validator_des.tree_of_dir_record(str(year), str(month), str(day))) < \
                                        len(obj_validator_scr.tree_of_dir_record(str(year), str(month), str(day))):
                                    print(f"[Destination][record]  - Different amount of records in month: {month} -> day {day}")
                                    print(f"[Destination][records] - {len(obj_validator_des.tree_of_dir_record(str(year), str(month), str(day)))}")
                                    print(f"[Source     ][records] - {len(obj_validator_scr.tree_of_dir_record(str(year), str(month), str(day)))}")
                                    for record in obj_validator_scr.tree_of_dir_record(str(year), str(month), str(day)):
                                        if record not in obj_validator_des.tree_of_dir_record(str(year), str(month), str(day)):
                                            obj_copy_paste = CopyPaste(str(obj_validator_des.path_day),
                                                                       str(obj_validator_scr.path_day))
                                            obj_copy_paste.copy_dir(str(record))
                else:
                    obj_validator_des.create_dir_month(str(month))
        else:
            obj_validator_des.create_dir_year(str(year))

# --- CleanUp & Zip AOI ---

    obj_validator_des = Validator(json_data['Path'][0]['DestinationZip'])
    if obj_validator_des.valid_path():
        print(f"[DestinationZip][{obj_validator_des.valid_path()}]    - {json_data['Path'][0]['DestinationZip']}")
    else:
        exit()
    obj_validator_scr = Validator(json_data['Path'][0]['SourceZip'])
    if obj_validator_scr.valid_path():
        print(f"[SourceZip     ][{obj_validator_scr.valid_path()}]    - {json_data['Path'][0]['SourceZip']}")
    else:
        exit()
    print(f"[DestinationZip][year]    - {obj_validator_des.tree_of_dir_year()}")
    print(f"[SourceZip     ][year]    - {obj_validator_scr.tree_of_dir_year()}")
    for year in obj_validator_scr.tree_of_dir_year()[-2:]:
        if year in obj_validator_des.tree_of_dir_year():
            print(f"[DestinationZip][month]   - {obj_validator_des.tree_of_dir_month(str(year))}")
            print(f"[SourceZip     ][month]   - {obj_validator_scr.tree_of_dir_month(str(year))}")

            for month in obj_validator_scr.tree_of_dir_month(str(year))[:-2]:  # TODO [:-2] !!!!!!!!!!!!!!
                if month not in obj_validator_des.tree_of_dir_month(str(year)):
                    obj_validator_des.create_dir_month(str(month))
                print(f"[SourceZip     ][monthPrepareToZip]   - {month}")

                for day in obj_validator_scr.tree_of_dir_day(str(year), str(month)):
                    if day + ".zip" not in obj_validator_des.tree_of_dir_day(str(year), str(month)):
                        print(f"[SourceZip     ][dayPrepareToZip]   - Src: {day} does not exist in Dst")

                        for record in obj_validator_scr.tree_of_dir_record(str(year), str(month), str(day)):
                            obj_copy_paste = CopyPaste(str(obj_validator_des.path_month),  # it is not use
                                                       str(obj_validator_scr.path_day))
                            obj_copy_paste.prepare_to_zip(record)

                        obj_copy_paste = CopyPaste(str(obj_validator_des.path_month),
                                                   str(obj_validator_scr.path_month))
                        obj_copy_paste.zip_day(day)

        else:
            obj_validator_des.create_dir_year(str(year))

# --- Copy AXI ---
    obj_validator_des = Validator(json_data['Path'][0]['DestinationAXI'])
    if obj_validator_des.valid_path():
        print(f"[DestinationAXI][{obj_validator_des.valid_path()}]    - {json_data['Path'][0]['DestinationAXI']}")
    else:
        exit()
    obj_validator_scr = Validator(json_data['Path'][0]['SourceAXI'])
    if obj_validator_scr.valid_path():
        print(f"[SourceAXI     ][{obj_validator_scr.valid_path()}]    - {json_data['Path'][0]['SourceAXI']}")
    else:
        exit()
    print(f"[DestinationAXI][year]    - {obj_validator_des.tree_of_dir_year()}")
    print(f"[SourceAXI     ][year]    - {obj_validator_scr.tree_of_dir_year()}")

    for year in obj_validator_scr.tree_of_dir_year():
        if year in obj_validator_des.tree_of_dir_year():
            print(f"[DestinationAXI][month]   - {obj_validator_des.tree_of_dir_month(str(year))}")
            print(f"[SourceAXI     ][month]   - {obj_validator_scr.tree_of_dir_month(str(year))[-2:]}")

            for month in obj_validator_scr.tree_of_dir_month(str(year))[-2:]:  # TODO [-2:]
                if month in obj_validator_des.tree_of_dir_month(str(year)):
                    if len(obj_validator_des.tree_of_dir_day(str(year),
                                                             str(month))) < \
                            len(obj_validator_scr.tree_of_dir_day(str(year),
                                                                  str(month))):
                        print(f"[DestinationAXI][day]     - Missing day in {month} month:")
                        for day in obj_validator_scr.tree_of_dir_day(str(year), str(month)):
                            if day not in obj_validator_des.tree_of_dir_day(str(year), str(month)):
                                print(f"                          day: {day}. Coping dir...")
                                obj_copy_paste = CopyPaste(str(obj_validator_des.path_month),
                                                           str(obj_validator_scr.path_month))
                                obj_copy_paste.copy_dir(str(day))
                            else:
                                if len(obj_validator_des.tree_of_dir_record(str(year), str(month), str(day))) < \
                                        len(obj_validator_scr.tree_of_dir_record(str(year), str(month), str(day))):
                                    print(f"[DestinationAXI][record]  - Different amount of records in month: {month} -> day {day}")
                                    print(f"[DestinationAXI][records] - {len(obj_validator_des.tree_of_dir_record(str(year), str(month), str(day)))}")
                                    print(f"[SourceAXI     ][records] - {len(obj_validator_scr.tree_of_dir_record(str(year), str(month), str(day)))}")
                                    for record in obj_validator_scr.tree_of_dir_record(str(year), str(month), str(day)):
                                        if record not in obj_validator_des.tree_of_dir_record(str(year), str(month), str(day)):
                                            obj_copy_paste = CopyPaste(str(obj_validator_des.path_day),
                                                                       str(obj_validator_scr.path_day))
                                            obj_copy_paste.copy_dir(str(record))
                else:
                    obj_validator_des.create_dir_month(str(month))
        else:
            obj_validator_des.create_dir_year(str(year))
