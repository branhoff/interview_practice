def min_meeting_rooms_wrong(meeting_times):
    if not meeting_times:
        return 0

    meeting_times.sort(key=lambda x: x[0])

    rooms_needed = 1
    prev_end_time = meeting_times[0][1]

    for i in range(1, len(meeting_times)):
        current_start, current_end = meeting_times[i]

        if current_start >= prev_end_time:
            prev_end_time = current_end
        else:
            rooms_needed += 1

    return rooms_needed


def min_meeting_rooms_2(meeting_times):
    if not meeting_times:
        return 0

    meeting_times.sort(key=lambda x: x[0])

    end_times = [meeting_times[0][1]]

    for i in range(1, len(meeting_times)):
        current_start, current_end = meeting_times[i]

        end_times.sort()

        if current_start >= end_times[0]:
            end_times[0] = current_end
        else:
            end_times.append(current_end)

    return len(end_times)

if __name__ == "__main__":
    print(min_meeting_rooms_wrong([[1,6],[2,3],[4,6],[5,9],[9,10],[7,12]]))
    print(min_meeting_rooms_2([[1,6],[2,3],[4,6],[5,9],[9,10],[7,12]]))

