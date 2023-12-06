from pprint import pprint

lines = open("input.txt").read()

def parse(lines):
    sections = lines.split("\n\n")
    seeds = [int(i) for i in sections[0].split(": ")[1].split()]
    maps = {}
    for sec in sections[1:]:
        sec = sec.split("\n")
        frm, to = sec[0].split()[0].split("-to-")
        maps[(frm, to)] = [[int(n) for n in m.split()] for m in sec[1:]]
    return seeds, maps

{("fertilizer", "water"): [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
 ("humidity", "location"): [[60, 56, 37], [56, 93, 4]],
 ("light", "temperature"): [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
 ("seed", "soil"): [[50, 98, 2], [52, 50, 48]],
 ("soil", "fertilizer"): [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
 ("temperature", "humidity"): [[0, 69, 1], [1, 0, 69]],
 ("water", "light"): [[88, 18, 7], [18, 25, 70]]}

def p1(lines):
    seeds, maps = parse(lines)
    def map(srccat, srcnum):
        """ Ret: dstcat, dstnum """
        dstcat = next(d for s, d in maps.keys() if s == srccat)
        ranges = maps[(srccat, dstcat)]
        for dststartrange, srcstartrange, rangelength in ranges:
            if srcnum >= srcstartrange and srcnum < srcstartrange + rangelength:
                return dstcat, dststartrange + (srcnum - srcstartrange)
        else:
            return dstcat, srcnum
    minloc = 99999999999999
    for seed in seeds:
        cat = "seed"
        num = seed
        while cat != "location":
            print(f"{cat}:{num} ", end="")
            cat, num = map(cat, num)
        minloc = min(num, minloc)
    return minloc

def p1_rec(lines):
    seeds, maps = parse(lines)
    def find_location(srccat, srcnum):
        """ Ret: location_number """
        if srccat == "location":
            return srcnum
        dstcat = next(d for s, d in maps.keys() if s == srccat)
        ranges = maps[(srccat, dstcat)]
        for dststartrange, srcstartrange, rangelength in ranges:
            if srcnum >= srcstartrange and srcnum < srcstartrange + rangelength:
                dstnum = dststartrange + (srcnum - srcstartrange)
                return find_location(dstcat, dstnum)
        else:
            return find_location(dstcat, srcnum)

    minloc = 99999999999999
    for seed in seeds:
        num = find_location("seed", seed)
        minloc = min(num, minloc)
    return minloc

print(p1_rec(lines))

def p2(lines):
    seeds, maps = parse(lines)
    seeds = list(zip(seeds[::2], seeds[1::2]))
    def find_min_location(srccat, src_start, src_len):
        """ Ret: minimum location_number """
        if srccat == "location":
            return src_start
        dstcat = next(d for s, d in maps.keys() if s == srccat)
        map_ranges = maps[(srccat, dstcat)]
        src_ranges = [(src_start, src_len)]

        minloc = 99999999999999

        for map_dst_start, map_src_start, map_len in map_ranges:
            map_src_end = map_src_start + map_len
            newsrc_ranges = []
            for src_start, src_len in src_ranges:
                src_end = src_start + src_len
                # Note: There is always
                #  - 0 or 1 mapped range
                #  - 0, 1 or 2 parts of the map that are not needed for the mapping
                #  - 0, 1 or 2 parts of the src that are not mapped

                cuts = sorted([src_start, src_end, map_src_start, map_src_end])
                for start, end in zip(cuts[:-1], cuts[1:]):
                    if start != end: # length > 0 (list is sorted, so start <= end is always true)
                        if src_start <= start and end <= src_end:  # inside src range
                            if map_src_start <= start and end <= map_src_end:  # inside map ranged
                                dst_start = map_dst_start + (start - map_src_start)
                                dst_len = end - start
                                minloc = min(minloc, find_min_location(dstcat, dst_start, dst_len))
                            else: # not part of this range -> try other ranges or res
                                newsrc_ranges.append((start, end - start))
                        else:
                            pass # not part of src -> part of map -> ignore
                    else:
                        pass # empty range

            src_ranges = newsrc_ranges

        # remaining src_ranges are mapped 1:1
        for src_start, src_len in src_ranges:
            minloc = min(minloc, find_min_location(dstcat, src_start, src_len))

        return minloc

    minloc = 99999999999999
    for seedrangestart, seedrangelength in seeds:
        num = find_min_location("seed", seedrangestart, seedrangelength)
        minloc = min(num, minloc)
    return minloc

print(p2(lines))
