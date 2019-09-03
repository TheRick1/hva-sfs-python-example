from api.amsterdam_api import AmsterdamApi


def main():
    amsterdam_api = AmsterdamApi()
    list_trash_bins = amsterdam_api.get_trash_bins()

    print("Overview of trash bins in Amsterdam")

    total = 0
    paper = 0
    residual_waste = 0

    for trash_bin in list_trash_bins:
        total += 1
        if trash_bin['type'] == 'Papier':
            paper += 1
        elif trash_bin['type'] == 'Rest':
            residual_waste += 1
        print(
            str(trash_bin['id']) + "\t" +
            trash_bin['name'] + "\t" +
            trash_bin['type'] + "\t" +
            trash_bin['address']
        )
    print('\nTotal amount of trash bins = ' + str(total))
    print('Total residual waste = ' + str(residual_waste))
    print('Total paper waste = ' + str(paper))


if __name__ == "__main__":
    main()
