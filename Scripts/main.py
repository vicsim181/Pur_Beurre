"""Main file from which the other scripts will be called."""
import dbcreation, creationcategories, dbfeed

if __name__ == '__main__':
    dbcreation.main()
    creationcategories.main()
    dbfeed.main()