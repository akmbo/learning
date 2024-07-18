package concurrency

import "sync"

type WebsiteChecker func(string) bool

func CheckWebsites(wc WebsiteChecker, urls []string) map[string]bool {
	results := make(map[string]bool)

	wg := sync.WaitGroup{}
	mu := sync.Mutex{}
	wg.Add(len(urls))

	for _, url := range urls {
		go func(u string) {
			result := wc(u)
			mu.Lock()
			results[u] = result
			mu.Unlock()
			wg.Done()
		}(url)
	}

	wg.Wait()

	return results
}
