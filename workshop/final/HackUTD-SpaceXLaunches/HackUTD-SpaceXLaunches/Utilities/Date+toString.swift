//
//  Date+toString.swift
//  HackUTD-SpaceXLaunches
//
//  Created by Nihaal Manesia on 11/11/24.
//

import Foundation

extension Date {
    /// Just a simple convenience function
    /// Takes a date object and uses DateFormatter to return a long style String
    func toString() -> String {
        let df = DateFormatter()
        df.dateStyle = .long
        return df.string(from: self)
    }
}
