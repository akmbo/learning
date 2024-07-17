package main

type Dictionary map[string]string

const (
	ErrNotFound   = DictionaryErr("could not find the word you were looking for")
	ErrWordExists = DictionaryErr("word already exists")
)

type DictionaryErr string

func (e DictionaryErr) Error() string {
	return string(e)
}

func (d Dictionary) Search(word string) (string, error) {
	result, ok := d[word]
	if ok {
		return result, nil
	}
	return "", ErrNotFound
}

func (d Dictionary) Add(word string, definition string) error {
	_, err := d.Search(word)

	switch err {
	case ErrNotFound:
		d[word] = definition
	case nil:
		return ErrWordExists
	default:
		return err
	}

	return nil
}
