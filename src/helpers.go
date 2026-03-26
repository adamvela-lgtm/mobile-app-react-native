package helpers

import (
	"crypto/rand"
	"encoding/hex"
	"errors"
	"strings"
	"time"
)

// GenerateRandomString generates a random string of the specified length.
func GenerateRandomString(length int) (string, error) {
	if length <= 0 {
		return "", errors.New("length must be greater than 0")
	}
	bytes := make([]byte, length)
	if _, err := rand.Read(bytes); err != nil {
		return "", err
	}
	return hex.EncodeToString(bytes)[:length], nil
}

// FormatTimestamp formats a time.Time value into a string with the specified layout.
func FormatTimestamp(t time.Time, layout string) string {
	return t.Format(layout)
}

// StringToBool converts a string representation of a boolean to a bool.
func StringToBool(s string) bool {
	s = strings.ToLower(strings.TrimSpace(s))
	return s == "true" || s == "1" || s == "t" || s == "y" || s == "yes"
}

// ContainsString checks if a string exists in a slice of strings.
func ContainsString(slice []string, s string) bool {
	for _, item := range slice {
		if item == s {
			return true
		}
	}
	return false
}

// RemoveDuplicates removes duplicate strings from a slice.
func RemoveDuplicates(slice []string) []string {
	keys := make(map[string]bool)
	var unique []string
	for _, entry := range slice {
		if _, value := keys[entry]; !value {
			keys[entry] = true
			unique = append(unique, entry)
		}
	}
	return unique
}